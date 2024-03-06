#!/usr/bin/python3


"""Pascal's Triangle
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal_rows = [[0, 1, 0]]
    for row in range(1, n):
        row_n = []
        try:
            for i in range(len(pascal_rows[row - 1]) + 1):
                row_n.append(pascal_rows[row - 1]
                             [i - 1] + pascal_rows[row - 1][i])
        except IndexError:
            row_n.append(pascal_rows[row - 1][i - 1])

        pascal_rows.append(row_n)

    return [row[1:-1] for row in pascal_rows]
