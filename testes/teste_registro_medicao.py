import csv
import io
import json
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import cv2
import numpy as np

from interface.aplicativo_angulo_contato import ContactAngleApp, _make_comparison_images
from processamento_imagem import filtros
from visualizacao import desenho


class TestRegistroMedicao(unittest.TestCase):
    def test_desenhar_tangente_aceita_lado_e_renderiza(self):
        canvas = MagicMock()
        contour = np.array([
            [20, 50], [30, 30], [50, 20], [70, 30], [80, 50], [80, 70], [20, 70],
        ], dtype=float)
        mask = np.zeros((80, 100), dtype=np.uint8)
        cv2.fillPoly(mask, [contour.astype(np.int32)], 255)

        desenho.desenhar_tangente_vetor(
            canvas,
            [20.0, 50.0],
            [0.0, -1.0],
            1.0,
            lambda x, y: (x, y),
            contour,
            50.0,
            mask,
            "esq",
        )

        canvas.create_line.assert_called_once()

    def test_excluir_registro_individual_atualiza_historico(self):
        record = {"sample": "Amostra"}
        history_button = MagicMock()
        master = MagicMock()
        app = SimpleNamespace(
            measurement_history=[record],
            measurement_record=record,
            history_button=history_button,
            master=master,
        )
        app._history_changed = lambda: ContactAngleApp._history_changed(app)

        removed = ContactAngleApp._delete_measurement_record(app, record)

        self.assertTrue(removed)
        self.assertEqual(app.measurement_history, [])
        self.assertIs(app.measurement_record, record)
        history_button.configure.assert_called_once_with(text="Histórico (0)")
        master._schedule_history_save.assert_called_once_with()

    def test_limpar_historico_remove_todas_as_medicoes(self):
        history_button = MagicMock()
        master = MagicMock()
        app = SimpleNamespace(
            measurement_history=[{"sample": "A"}, {"sample": "B"}],
            measurement_record={"sample": "B"},
            history_button=history_button,
            master=master,
        )
        app._history_changed = lambda: ContactAngleApp._history_changed(app)

        ContactAngleApp._clear_measurement_history(app)

        self.assertEqual(app.measurement_history, [])
        self.assertEqual(app.measurement_record, {"sample": "B"})
        history_button.configure.assert_called_once_with(text="Histórico (0)")
        master._schedule_history_save.assert_called_once_with()

    def test_tangente_fica_fora_da_mascara_nos_dois_contatos(self):
        angles = np.linspace(np.pi, 0, 120)
        arc = np.column_stack((
            50 + 30 * np.cos(angles),
            50 - 30 * np.sin(angles),
        ))
        contour = np.vstack((arc, [[80, 50], [20, 50]])).astype(float)
        mask = np.zeros((80, 100), dtype=np.uint8)
        cv2.fillPoly(mask, [np.rint(contour).astype(np.int32)], 255)

        for contact, lado in (
            ([20.0, 50.0], "esq"),
            ([80.0, 50.0], "dir"),
        ):
            segment = desenho.segmento_tangente_exterior(
                contact,
                [0.0, -1.0],
                contour,
                50.0,
                mask,
                25.0,
                lado,
            )

            self.assertIsNotNone(segment)
            self.assertLess(segment[1][1], contact[1])
            interior = cv2.erode(mask, np.ones((3, 3), dtype=np.uint8), iterations=1)
            for distance in np.arange(1.0, 25.0, 1.0):
                fraction = min(distance / np.linalg.norm(np.subtract(segment[1], segment[0])), 1.0)
                x = int(round(segment[0][0] + (segment[1][0] - segment[0][0]) * fraction))
                y = int(round(segment[0][1] + (segment[1][1] - segment[0][1]) * fraction))
                self.assertEqual(interior[y, x], 0)

    def test_tangente_escolhe_ramo_superior_independente_do_angulo(self):
        contour = np.array([
            [20, 50], [30, 30], [50, 20], [70, 30], [80, 50], [80, 70], [20, 70],
        ], dtype=float)
        mask = np.zeros((80, 100), dtype=np.uint8)
        cv2.fillPoly(mask, [contour.astype(np.int32)], 255)

        for lado, tangent, horizontal in (
            ("esq", [0.5, 0.866], False),
            ("dir", [-0.5, 0.866], False),
            ("esq", [1.0, 0.0], True),
            ("dir", [1.0, 0.0], True),
        ):
            contact = [20.0, 50.0] if lado == "esq" else [80.0, 50.0]
            segment = desenho.segmento_tangente_exterior(
                contact,
                tangent,
                contour,
                50.0,
                mask,
                20.0,
                lado,
            )

            self.assertIsNotNone(segment)
            if horizontal:
                if lado == "esq":
                    self.assertLess(segment[1][0], contact[0])
                else:
                    self.assertGreater(segment[1][0], contact[0])
            else:
                self.assertLess(segment[1][1], contact[1])

    def test_tangente_que_entraria_na_gota_e_ocultada(self):
        contour = np.array([
            [20, 50], [30, 30], [50, 20], [70, 30], [80, 50], [80, 70], [20, 70],
        ], dtype=float)
        mask = np.zeros((80, 100), dtype=np.uint8)
        cv2.fillPoly(mask, [contour.astype(np.int32)], 255)

        segment = desenho.segmento_tangente_exterior(
            [20.0, 50.0],
            [1.0, -0.25],
            contour,
            50.0,
            mask,
            25.0,
            "esq",
        )

        self.assertIsNone(segment)

    def test_imagem_final_comparativa_renderiza_as_duas_tangentes(self):
        angles = np.linspace(np.pi, 0, 120)
        contour = np.column_stack((
            50 + 30 * np.cos(angles),
            50 - 30 * np.sin(angles),
        )).astype(float)
        mask = np.zeros((80, 100), dtype=np.uint8)
        cv2.fillPoly(mask, [np.rint(contour).astype(np.int32)], 255)
        raw = np.zeros((80, 100, 3), dtype=np.uint8)

        panels = _make_comparison_images(
            raw,
            mask,
            contour,
            50.0,
            (1.0, 0.0, 0.0, 50.0),
            [20.0, 50.0],
            [80.0, 50.0],
            [0.0, -1.0],
            [0.0, -1.0],
            90.0,
            90.0,
            False,
            (5, 5),
        )
        final_image = panels["Resultado final (contatos, tangentes e ângulos)"]

        np.testing.assert_array_equal(final_image[30, 20], [0, 100, 255])
        np.testing.assert_array_equal(final_image[30, 80], [0, 100, 255])

    def test_historico_persiste_fora_da_sessao(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with patch.dict(os.environ, {"APPDATA": temporary_directory}):
                records = [{
                    "timestamp": "2026-10-24T21:00:00-03:00",
                    "status": "Concluída",
                    "image_sha256": "",
                    "sample": "Amostra 1",
                    "notes": "",
                    "source_name": "gota.png",
                    "source_path": "C:\\dados\\gota.png",
                    "acquisition_mode": "Arquivo",
                    "image_size": "640x480 px",
                    "analysis_size": "320x240 px",
                    "roi": [10, 20, 330, 260],
                    "filter_mode": "Auto",
                    "mask_source": "OTSU_BASE",
                    "mask_quality": 92.5,
                    "risk_flags": [],
                    "baseline_method": "floor_seeker_hybrid",
                    "contact_method": "validated_contact",
                    "baseline_y_px": 231.0,
                    "left_contact_px": [15.0, 230.0],
                    "right_contact_px": [310.0, 230.0],
                    "left_internal_deg": 99.62,
                    "left_external_deg": 80.38,
                    "right_internal_deg": 99.71,
                    "right_external_deg": 80.29,
                    "mean_internal_deg": 99.67,
                    "fit_score": 85.0,
                    "fit_rmse_px": 0.49,
                    "fit_points": 125,
                    "manual_adjustments": [],
                    "calculation_parameters": {},
                }]

                ContactAngleApp.save_measurement_history(records)

                self.assertEqual(ContactAngleApp.load_measurement_history(), records)

    def test_historico_vazio_persistido_apaga_registros_salvos(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with patch.dict(os.environ, {"APPDATA": temporary_directory}):
                ContactAngleApp.save_measurement_history([{"registro": "antigo"}])
                ContactAngleApp.save_measurement_history([])

                history_path = ContactAngleApp._measurement_history_path()
                self.assertEqual(json.loads(history_path.read_text(encoding="utf-8")), [])
                self.assertEqual(ContactAngleApp.load_measurement_history(), [])

    def test_exportacao_tabular_inclui_status_e_parametros(self):
        record = {
            "timestamp": "2026-10-24T21:00:00-03:00",
            "status": "Concluída",
            "image_sha256": "abc123",
            "sample": "Amostra 1",
            "notes": "",
            "source_name": "gota.png",
            "source_path": "C:\\dados\\gota.png",
            "acquisition_mode": "Arquivo",
            "image_size": "640x480 px",
            "analysis_size": "320x240 px",
            "roi": [10, 20, 330, 260],
            "filter_mode": "Auto",
            "mask_source": "OTSU_BASE",
            "mask_quality": 92.5,
            "risk_flags": [],
            "left_internal_deg": 99.62,
            "left_external_deg": 80.38,
            "right_internal_deg": 99.71,
            "right_external_deg": 80.29,
            "mean_internal_deg": 99.67,
            "baseline_method": "floor_seeker_hybrid",
            "baseline_y_px": 231.0,
            "left_contact_px": [15.0, 230.0],
            "right_contact_px": [310.0, 230.0],
            "contact_method": "validated_contact",
            "fit_score": 85.0,
            "fit_rmse_px": 0.49,
            "fit_points": 125,
            "manual_adjustments": [],
            "calculation_parameters": {"angle_contact_min_r2": 0.7},
        }

        rows = list(csv.reader(
            io.StringIO(ContactAngleApp._measurement_csv_text([record])),
            delimiter="\t",
        ))
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(rows[0]), len(rows[1]))
        self.assertIn("status", rows[0])
        parameters_index = rows[0].index("parametros_calculo_json")
        self.assertEqual(json.loads(rows[1][parameters_index]), {"angle_contact_min_r2": 0.7})

    def test_paineis_comparativos_mantem_etapas_e_tamanhos(self):
        raw = np.zeros((120, 180, 3), dtype=np.uint8)
        mask = np.zeros((120, 180), dtype=np.uint8)
        mask[20:100, 30:150] = 255
        contour = np.array(
            [[30, 100], [50, 40], [90, 20], [130, 40], [150, 100]],
            dtype=float,
        )

        panels = _make_comparison_images(
            raw,
            mask,
            contour,
            100,
            (1.0, 0.0, 0.0, 100.0),
            [30, 100],
            [150, 100],
            [0.8, -0.6],
            [-0.8, -0.6],
            99.0,
            100.0,
            True,
            (5, 5),
        )

        self.assertEqual(len(panels), 4)
        self.assertTrue(all(image.shape[:2] == (120, 180) for image in panels.values()))
        self.assertIn("Gaussian 5x5", list(panels)[1])
        self.assertTrue(np.all(raw == 0))

    def test_filtros_usa_kernels_e_limites_configurados(self):
        image = np.zeros((24, 32, 3), dtype=np.uint8)
        gaussian_kernels = []
        canny_thresholds = []

        def fake_gaussian_blur(gray, kernel, sigma):
            gaussian_kernels.append(kernel)
            return gray

        def fake_canny(gray, threshold_low, threshold_high):
            canny_thresholds.append((threshold_low, threshold_high))
            return np.zeros(gray.shape, dtype=np.uint8)

        with (
            patch.object(filtros.cv2, "GaussianBlur", side_effect=fake_gaussian_blur),
            patch.object(filtros.cv2, "Canny", side_effect=fake_canny),
        ):
            filtros.aplicar_filtro_binary_otsu(image)
            filtros.aplicar_filtro_edges_canny(image)

        self.assertEqual(gaussian_kernels, [filtros.OTSU_BLUR_KERNEL, filtros.CANNY_BLUR_KERNEL])
        self.assertEqual(
            canny_thresholds,
            [(filtros.CANNY_THRESHOLD_LOW, filtros.CANNY_THRESHOLD_HIGH)],
        )


if __name__ == "__main__":
    unittest.main()
