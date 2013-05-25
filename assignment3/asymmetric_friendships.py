__author__ = 'Robbie McDowall'
import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(friendship):
    person = friendship[0]
    friend = friendship[1]

    mr.emit_intermediate((friend, person), 1)


# Part 3
def reducer(couple, instances):
    if len(instances) == 1:
        mr.emit(couple)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
