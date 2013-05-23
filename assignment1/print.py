__author__ = 'Robbie McDowall'

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
response = json.load(response)

results = response["results"]

firstResult = results[0]

for i in range(0, 10):
    print results[i]