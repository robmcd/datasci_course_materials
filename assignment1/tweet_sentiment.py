import sys
import json
import unittest


def calculateSentiment(tweetText, sentimentScores):
    sentimentSum = 0
    for term in tweetText.split():
        if term in sentimentScores:
            sentimentSum += float(sentimentScores[term])
    return sentimentSum


def loadSentiments(sentimentFile):
    # sentiments are tab-delimited file of word(s) followed by a sentiment value (a float between -5.0 and 5.0)
    sentimentScores = {}
    for line in sentimentFile.readlines():
        entry = line.split()
        # sentiment might be a phrase, so we need to make sure to include the spaces
        sentimentValue = entry.pop()
        sentimentScores[' '.join(entry)] = sentimentValue
    return sentimentScores


def main():
    sentimentFile = open(sys.argv[1])
    tweetFile = open(sys.argv[2])
    sentimentScores = loadSentiments(sentimentFile)
    for line in tweetFile.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            print str(float(calculateSentiment(tweet["text"], sentimentScores)))


if __name__ == '__main__':
    main()
