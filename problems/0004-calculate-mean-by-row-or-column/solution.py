import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		ax = 1
	else:
		ax = 0

	return np.mean(matrix, axis=ax)