from collections import OrderedDict

__author__ = 'Robbie McDowall'

import sys
import json

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
    cumulativeStateHappinessScores = {}

    for line in tweetFile.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            state = getStateLocation(tweet)
            if state is not None:
                score = calculateSentiment(tweet["text"], sentimentScores)
                if state in cumulativeStateHappinessScores:
                    cumulativeStateHappinessScores[state] = cumulativeStateHappinessScores[state] + score
                else:
                    cumulativeStateHappinessScores[state] = score
    cumulativeStateHappinessScores = OrderedDict(sorted(cumulativeStateHappinessScores.items(), key=lambda t: t[1]))
    print cumulativeStateHappinessScores.keys()[0]


# returns the 2 letter USA state abbreviation for the state that this tweet came from
def getStateLocation(tweet):
    states = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",\
              "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD",\
              "TN","TX","UT","VT","VA","WA","WV","WI","WY","AS","GU","MP","PR","VI"]

    if "place" in tweet and tweet["place"] is not None and tweet["place"]["country_code"] == "US":
        for state in states:
            if tweet["place"]["full_name"].find(state) != -1:
                return state
    return None


if __name__ == '__main__':
    main()
