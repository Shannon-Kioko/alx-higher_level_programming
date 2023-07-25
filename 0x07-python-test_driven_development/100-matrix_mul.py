def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and return the result.

    Args:
        m_a (list of lists): The first matrix represented as a list of lists
        of integers or floats.
        m_b (list of lists): The second matrix represented as a list
        of lists of integers or floats.

    Returns:
        list of lists: The result of multiplying the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists,
        or if an element is not an integer or a float.
        ValueError: If m_a or m_b is empty or not a rectangle (all rows
        should be of the same size).
                    If m_a and m_b can't be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not
           all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a "
                        "list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) \
       or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats "
                        "or m_b should contain only integers or floats")

    a_rows, a_cols = len(m_a), len(m_a[0])
    b_rows, b_cols = len(m_b), len(m_b[0])

    if any(len(row) != a_cols for row in m_a) or any(len(row) != b_cols for row in m_b):
        raise TypeError("each row of m_a must be of the same size "
                        "or each row of m_b must be of the same size")

    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
