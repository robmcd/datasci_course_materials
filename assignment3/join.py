__author__ = 'Robbie McDowall'
import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    orderId = record[1]
    mr.emit_intermediate(orderId, record)


# Part 3
def reducer(orderId, records):
    orders = []
    lines = []
    for r in records:
        tableName = r[0]
        if tableName == "order":
            orders.append(r)
        else:
            lines.append(r)
    for order in orders:
        for line in lines:
            mr.emit(order + line)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
