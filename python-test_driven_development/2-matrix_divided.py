#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor and return a new matrix.

    Args:
        matrix (list of lists): The matrix to be divided, containing integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                  if the rows are not all the same size,
                  or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with elements divided by div and rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check each element in the matrix is an integer or float
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows have the same length
    if matrix:
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError(
                    "Each row of the matrix must have the same size")

    # Check div is a number (int or float)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    # Check div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with each element divided by div and rounded to 2 decimals
    return [[round(element / div, 2) for element in row] for row in matrix]
