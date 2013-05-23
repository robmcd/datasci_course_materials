__author__ = 'Robbie McDowall'

import urllib
import json

for i in range(1, 11):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(i))
    response = json.load(response)

    results = response["results"]

    for result in results:
        print result["text"]