#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for col in matrix:
        x = [x**2 for x in matrix]
        copy.append(x)
    return copy
