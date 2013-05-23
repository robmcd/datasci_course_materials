import sys
import json
import csv

# will normalize (change spread to be between -5 and 5) the dictionary entries by value
def scale(dict):
    maxVal = max(dict.values())
    minVal = min(dict.values())
    for key in dict.iterkeys():
        if dict[key] > 0:
            dict[key] = (float(dict[key]) / maxVal) * 5
        else:
            dict[key] = (float(dict[key]) / minVal) * -5
    return dict

# sentimentScore is the sum of the sentiment of each term in the tweet
def calcSentiment(tweetText, *sentimentScores):
    sentimentSum = 0
    for term in tweetText.split():
        for s in sentimentScores:
            if term in s:
                sentimentSum += float(s[term])
                break
    return sentimentSum


def loadSentiments(sentimentFile):
    # sentiments are tab-delimited file of word(s) followed by a sentiment value (a float between -5.0 and 5.0)
    sentimentScores = {}
    for line in sentimentFile.readlines():
        entry = line.split()
        # sentiment might be a phrase, so we need to make sure to include the spaces
        sentimentValue = float(entry.pop())
        sentimentScores[' '.join(entry)] = sentimentValue
    return sentimentScores


def updateScoresWithDerivedSentiments(newScores, refScores, tweet):
    dicts = (refScores, {})
    if calcSentiment(tweet, *dicts) > 0:
        incTermSentiments(newScores, refScores, tweet.split())
    elif calcSentiment(tweet, *dicts) < 0:
        decTermSentiments(newScores, refScores, tweet.split())
    else:
        zeroTermSentiments(newScores, refScores, tweet.split())
    return newScores


def zeroTermSentiments(newSentimentScores, referenceSentimentScores, terms):
    for term in terms:
        if term not in referenceSentimentScores:
            newSentimentScores[term] = 0


def incTermSentiments(newSentimentScores, referenceSentimentScores, terms):
    for term in terms:
        if term not in referenceSentimentScores:
            if term in newSentimentScores:
                newSentimentScores[term] = float(newSentimentScores[term]) + 1
            else:
                newSentimentScores[term] = 1


def decTermSentiments(newSentimentScores, referenceSentimentScores, terms):
    for term in terms:
        if term not in referenceSentimentScores:
            if term in newSentimentScores:
                newSentimentScores[term] = float(newSentimentScores[term]) - 1
            else:
                newSentimentScores[term] = -1


def main():
    sentimentFile = open(sys.argv[1])
    tweetFile = open(sys.argv[2])
    baselineSentimentScores = loadSentiments(sentimentFile)
    newSentimentScores = dict(baselineSentimentScores)

    printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for line in tweetFile.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            tweetContent = tweet["text"]
            tweetContent = filter(lambda x: x in printable, tweetContent)
            updateScoresWithDerivedSentiments(newSentimentScores, baselineSentimentScores, tweetContent)

    # scale(newSentimentScores)
    with open('sentiments.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect=csv.excel)
        writer.writerow(["term", "sentiment"])
        for term, sentiment in newSentimentScores.iteritems():
            if type(term) == unicode:
                print term.encode("utf-8") + " " + str(sentiment)
                writer.writerow([term.encode("utf-8"), str(sentiment)])

if __name__ == '__main__':
    main()
