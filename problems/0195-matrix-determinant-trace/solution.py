def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	n = len(matrix[0])
	trace = sum(matrix[i][i] for i in range(n))
	
	def determinant(mat, n, i=0):
		match n:
			case 1:
				det = mat[0]
			case 2:
				det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
			case _:
				det = sum((-1) ** j * mat[0][j] * determinant([row[:j] + row[j+1:] for row in mat[1:]], n-1) for j in range(n))		
		return det

	
	return (determinant(matrix, n), trace)