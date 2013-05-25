'''
Problem 1
Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with
a list of the document identifiers in which that word appears.

Mapper Input
The input is a 2 element list: [document_id, text]
document_id: document identifier formatted as a string
text: text of the document formatted as a string
The document text may have words in various cases or elements of punctuation. Do not modify the string, and treat each
token as if it was a valid word. (That is, just use value.split())

Reducer Output
The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.
You can test your solution to this problem using books.json:
        python inverted_index.py books.json
You can verify your solution against inverted_index.json.
'''


__author__ = 'Robbie McDowall'
import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(doc):
    # key: document identifier
    # value: document contents
    docId = doc[0]
    value = doc[1]
    words = value.split()
    emmitedWords = []
    for w in words:
        if w not in emmitedWords:
            mr.emit_intermediate(w, docId)
        emmitedWords.append(w)


# Part 3
def reducer(word, docs):
    mr.emit((word, docs))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)