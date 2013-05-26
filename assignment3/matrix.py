__author__ = 'Robbie McDowall'

import sys
import operator

import MapReduce


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
# A has dimendions LxM
# B has dimensions MxN

# assume dimensions are 5 by 5 for both A and B matrices
    L = 5
    M = 5
    N = 5

    matrixName = record[0]
    value = record[3]

    if matrixName == "a":
        i = record[1]
        j = record[2]
        for k in xrange(N):
            mr.emit_intermediate((i, k), (matrixName, i, j, value))
    elif matrixName == "b":
        j = record[1]
        k = record[2]
        for q in xrange(L):
            mr.emit_intermediate((q, k), (matrixName, j, k, value))


def reducer(key, cells):
    rowFromA = []
    columnFromB = []
    for cell in cells:
        matrixName = cell[0]
        rowIdx = cell[1]
        colIdx = cell[2]
        value = cell[3]
        if matrixName == "a":
            rowFromA.append((rowIdx, colIdx, value))
        elif matrixName == "b":
            columnFromB.append((rowIdx, colIdx, value))

    products = []
    for a in rowFromA:
        for b in columnFromB:
            if a[1] == b[0]:   # col from A matches row from B
                products.append(a[2] * b[2])
                break

    mr.emit((key[0], key[1], reduce(operator.add, products)))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
