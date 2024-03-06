import math


"""Pascal's Triangle
"""


def nCr(row, col):
    """
        get pascal coeficient for nth row, rth column
        where r <= n
    """
    return (math.factorial(row) //
            (math.factorial(col) * (math.factorial(row - col))))


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    return [
        [nCr(row, r) for r in range(row)]
        for row in range(n)
    ]
