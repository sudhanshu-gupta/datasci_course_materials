#!/usr/bin/python

from __future__ import division
from collections import Counter
import json
import sys

__author__ = 'sudhanshu.gupta'

def hash_tags(tweet_file):
    with open(tweet_file) as f:
        entities = (json.loads(line).get('entities', None) for line in f);
        hashtags = (entity.get('hashtags') for entity in entities if entity);
        texts = (tag['text'] for tags in hashtags for tag in tags)
        return Counter(texts).most_common(10);



if __name__ == '__main__':
    top_ten_tags = hash_tags(tweet_file=sys.argv[1]);
    sys.stdout.writelines("{0} {1}.0\n".format(tag.encode('utf-8'), count) for tag, count in top_ten_tags)
