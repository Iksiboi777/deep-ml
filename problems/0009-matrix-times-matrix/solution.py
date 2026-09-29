import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    # a_np = np.array(a)
    # b_np = np.array(b)

    # if a_np.shape[1] != b_np.shape[0]:
    #     return -1
	
    # return np.matmul(a, b).tolist()
    if len(list(zip(*a))) != len(b):
        return -1

    return [[sum([x*y for x,y in zip(row1, row2)]) for row2 in zip(*b)] for row1 in a]