import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	# c = []
	if len(a) != len(b):
		return -1
	c = np.array(a) + np.array(b)
	return c.tolist()
	

		# if len(a) == len(b):
	# 	for i range(len(a)):
	# 	c.append(a[i] + b[i])