#!/usr/bin/python3
'''Island perimeter'''


def island_perimeter(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    perimeter = 0

    for r in range(row_len):
        for c in range(col_len):
            if grid[r][c] == 1:
                perimeter = perimeter + 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter = perimeter - 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter = perimeter - 2

    return perimeter
