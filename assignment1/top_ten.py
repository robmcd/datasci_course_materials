from collections import OrderedDict
import json
import sys

__author__ = 'Robbie McDowall'



def main():
    tweetFile = open(sys.argv[1])

    hashtagCounts = {}

    for line in tweetFile.readlines():
        tweet = json.loads(line)
        if "entities" in tweet and tweet["entities"]["hashtags"] is not None:
            for hashtag in tweet["entities"]["hashtags"]:
                tag = hashtag["text"]
                if type(tag) != unicode:
                    continue
                if tag in hashtagCounts:
                    hashtagCounts[tag] = hashtagCounts[tag] + 1
                else:
                    hashtagCounts[tag] = 1

    hashtagCounts = OrderedDict(reversed(sorted(hashtagCounts.items(), key=lambda t: t[1])))
    # hashtagCounts.reverse()
    for i in range(10):
        print hashtagCounts.keys()[i].encode("utf-8"), hashtagCounts[hashtagCounts.keys()[i]]


if __name__ == '__main__':
    main()
