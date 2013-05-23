__author__ = 'Robbie McDowall'

import unittest
from tweet_sentiment import *


class MyTest(unittest.TestCase):
    def testLoadSentiments(self):
        sentimentFile = open("AFINN-111.txt")
        sentimentScores = loadSentiments(sentimentFile)
        sentimentFile.seek(0)
        sentimentFileLines = sentimentFile.readlines()
        self.assertEqual(len(sentimentFileLines), len(sentimentScores.keys()))

        sentimentFileLinesReconstructed = []
        for sentiment, score in sentimentScores.iteritems():
            sentimentFileLinesReconstructed.append(sentiment + "\t" + score + "\n")

        self.assertEqual(len(set(sentimentFileLines)),
                         len(set(sentimentFileLines).intersection(set(sentimentFileLinesReconstructed))) + 1)