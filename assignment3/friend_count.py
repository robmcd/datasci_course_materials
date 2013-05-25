__author__ = 'Robbie McDowall'
import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(friendship):
    person = friendship[0]
    friend = friendship[1]

    mr.emit_intermediate(person, friend)


# Part 3
def reducer(person, friends):
    mr.emit((person, len(friends)))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
