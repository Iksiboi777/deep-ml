import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape:
		raise ValueError("Arrays must have the same shape!")
	if v1.size == 0:
		raise ValueError("Arrays cannot be the empty!")

	v1_flat = v1.flatten()
	v2_flat = v2.flatten()

	mag1 = np.linalg.norm(v1_flat, ord=2)
	mag2 = np.linalg.norm(v2_flat, ord=2)

	if mag1 == 0 or mag2 == 0:
		raise ValueError("Vectors have ZERO magnitude!")
	
	return np.dot(v1_flat, v2_flat) / (mag1*mag2)