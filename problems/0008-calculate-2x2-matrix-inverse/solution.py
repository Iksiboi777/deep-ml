def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    mat = matrix.copy()
    a = mat[0][0]
    b = mat[0][1]
    c = mat[1][0]
    d = mat[1][1]

    det = a*d - b*c
    if det == 0:
        return None
    
    return [[d/det, -b/det],
            [-c/det, a/det]]
