def square_matrix_simple(matrix=[]):
    """
    Computes square values of all integers of a matrix
    """
    new_m = matrix.copy()
    for i, row in enumerate(new_m):
            new_m[i] = list(map(lambda x: x**2, row))
    return new_m
