#!/usr/bin/python3
""""calculate perimeter of an island grid"""


def island_perimeter(grid):
    """calculate the perimeter of an island grid"""
    x_len = len(grid)
    y_len = len(grid[0])
    perimeter = 0
    for x in range(x_len):
        for y in range(y_len):
            perimeter += get_perimeter(y, x, grid)

    return perimeter


def get_perimeter(y, x, grid):
    """get perimeter of a single cell"""
    perimeter = 0
    idx = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    if (grid[x][y]):
        for id in idx:
            if id[0] < 0 or id[1] < 0:
                perimeter += 1
                continue
            try:
                if not grid[id[0]][id[1]]:
                    perimeter += 1
            except Exception:
                perimeter += 1
    return (perimeter)
