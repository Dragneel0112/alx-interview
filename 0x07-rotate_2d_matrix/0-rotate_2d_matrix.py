#!/usr/bin/python3
'''
Rotates a 2D matrix 90 degrees
'''


def rotate_2d_matrix(matrix):
    '''
    Rotates 2D matrix in place
    '''
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda x: len(x) == columns, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(columns * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == columns - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
