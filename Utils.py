import numpy as np


def get_max(S):
    pos = 0
    max = 0
    for row in S:
        for i in range(0, len(row)):
            if max < row[i]:
                max = row[i]
                pos = i
    return max, pos


def get_sum(D):
    result = []
    D = np.asarray(D)
    for raw in D:
        presum = 0
        for column in raw:
            if column:
                presum += 1

        result.append(presum)

    return np.asmatrix(result)


def append_to_matrix(matrix, element):
    if isinstance(matrix, list):
        m = matrix
    else:
        m = list(np.array(np.transpose(matrix)).reshape(-1,))

    if isinstance(element, list):
        m = m + element
    else:
        m = m + [element]
    return np.transpose(np.matrix(m))
