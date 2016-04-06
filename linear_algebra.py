import math
class ShapeError(Exception):
    pass


def shape(vector_matrix):
    rows = len(vector_matrix)
    if type(vector_matrix[0]) == type([]):
        columns = len(vector_matrix[0])
        return (rows, columns)
    else:
        return (rows, )

def vector_add(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        added_vectors = [a + b for a, b in zip(vector_one, vector_two)]
    else:
        raise ShapeError("Cannot add vectors of different dimensions")
    return added_vectors

def vector_sub(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        subtracted_vectors = [a - b for a, b in zip(vector_one, vector_two)]
    else:
        raise ShapeError("Cannot subtract vectors of different dimensions")
    return subtracted_vectors

def vector_sum(*args):
    shape_results = [shape(vector) for vector in args] #put the number of rows of each vector into a list
    if max(shape_results) == min(shape_results): #count the number of vectors that have the same amount of rows. True if equal to number of vectors.
        #list_of_tuples = zip(vector_list)
        summed_vectors = [sum(a) for a in zip(*args)]
    else:
        raise ShapeError("Cannot sum vectors of different dimensions")
    return summed_vectors

def dot(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        dot_product = sum(a*b for a, b in zip(vector_one, vector_two))
    else:
        raise ShapeError("Cannot multiply vectors of different dimensions")
    return dot_product

def vector_multiply(vector, scalar):
    return [number * scalar for number in vector]

def mean(*args):
    return sum(*args) / len(*args)

def vector_mean(*args):
    return [mean(a) for a in zip(*args)]

def magnitude(vector):
    return math.sqrt((sum([number**2 for number in vector])))

def matrix_row(matrix, row):
    return matrix[row]

def matrix_col(matrix, col):
    return [row[col] for row in matrix]
