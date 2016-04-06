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
        added_vectors = [a+b for a, b, in zip(vector_one, vector_two)]
    else:
        raise ShapeError("Cannot add vectors of different dimensions")
    return added_vectors
