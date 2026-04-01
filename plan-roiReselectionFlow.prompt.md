1. Em main.py, manter o processamento na ROI, mas desenhar o preview sobre cópia da imagem inteira (self.raw_image.copy()), deslocando os pontos por (x1, y1).

2. Em main.py, manter render_frame() com preview do mesmo tamanho da imagem original.

3. Em main.py, adicionar guarda para ROI mínima (ex.: 5 px) para evitar clique acidental.

4. Em main.py, redesenhar o retângulo da ROI após canvas.delete("all"), para permitir ajuste várias vezes sem perder referência visual.
