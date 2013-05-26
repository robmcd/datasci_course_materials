__author__ = 'Robbie McDowall'

import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    bps = str(record[1])
    trimmed = bps[:-10]
    mr.emit_intermediate(trimmed, None)


def reducer(key, list_of_values):
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
