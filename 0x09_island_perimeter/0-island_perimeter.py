#!/usr/bin/python3
"""
  function that returns the perimeter of the island described in grid
  0 water ,1 land, cell is square(1*1) horizontally or vertically no diagonal
 """


def island_perimeter(grid):
    length_row = len(grid)
    length_column = len(grid[0])

    p = 0
    connections = 0

    for x in range(0, length_row):
        for y in range(0, length_column):

            if grid[x][y] == 1:
                p += 4

            if x != 0 and grid[x - 1][y] == 1:
                connections += 1
            if y != 0 and grid[x][y - 1] == 1:
                connections += 1
    return p - (connections * 2)
