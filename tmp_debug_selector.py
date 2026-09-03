import numpy as np
import warnings
import math
from Cal_angulo import angulo_contato

contour = np.array([
    [0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0], [4.0, 4.0], [5.0, 5.0],
    [6.0, 6.0], [7.0, 7.0], [8.0, 8.0], [9.0, 9.0], [10.0, 10.0], [11.0, 11.0],
    [12.0, 12.0], [13.0, 13.0], [14.0, 14.0], [15.0, 15.0], [16.0, 16.0], [17.0, 17.0],
    [18.0, 18.0], [19.0, 19.0],
], dtype=float)
contact = [8.0, 8.0]
result = angulo_contato._selecionar_pontos_tangente(contour, 10.0, contact, contour)
print(result)
print([int(np.where((contour == pt).all(axis=1))[0][0]) for pt in result])
