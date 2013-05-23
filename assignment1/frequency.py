from collections import OrderedDict
import json
import sys

__author__ = 'Robbie McDowall'

def main():
    tweetFile = open(sys.argv[1])
    termCounts = {}
    numOccurances = 0
    for line in tweetFile.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            for term in tweet["text"].split():
                numOccurances += 1
                if term in termCounts:
                    termCounts[term] = termCounts[term] + 1
                else:
                    termCounts[term] = 1

    # termCounts = OrderedDict(sorted(termCounts.items(), key=lambda t: t[1]))
    for term, freq in termCounts.iteritems():
        if type(term) == unicode:
            print term.encode("utf-8"), str(float(freq / numOccurances))

if __name__ == '__main__':
    main()
