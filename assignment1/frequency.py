#!/usr/bin/python

from __future__ import division
import sys
import json
from collections import Counter

def get_frequency(tweet_file):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f)
        return Counter(word for tweet in tweets if tweet for word in tweet)


if __name__ == "__main__":
    frequencies = get_frequency(sys.argv[1])
    length = sum(frequencies.values())
    sys.stdout.writelines("{0} {1}\n".format(word.encode('utf-8'), frequencies[word]/length) for word in frequencies)
