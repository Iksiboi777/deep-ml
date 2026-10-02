import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    k = len(vectors)
    dims = {len(v) for v in vectors}
    same = len(dims) == 1

    if len(vectors) == 0:
        return True

    if same:
        d = len(vectors[0])
        if k > d:
            return False # you cannot have more vectors than dimensions

        if d == 1 and any(x != 0 for x in vectors[0]):
            return True # A single non zero vector is always linearly independent
        
        M = [list(map(float, v)) for v in vectors]
        rank = 0
        if all(v < 1e-6 for v in M[rank]):
            return False # no zero vectors allowed

        for col in range(d):
            pivot = max(range(rank, k), key=lambda r: abs(M[r][col]))

            M[rank], M[pivot] = M[pivot], M[rank]
            for r in range(rank + 1, k):
                factor = M[r][col] / M[rank][col]
                for c in range(col, d):
                    M[r][c] -= factor * M[rank][c]
                if all(abs(v) < 1e-6 for v in M[r]):
                    return False # Vectors are colinear, linearly dependent
            rank += 1
            if rank == k:
                break

        return rank == k
    else:
        raise ValueError ("The vectors have different lengths!")