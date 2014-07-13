#!/usr/bin/python

import sys
import json

def built_score(sent_file):
    scores = {};
    for line in sent_file:
        term, score = line.split('\t');
        scores[term] = int(score);
    return scores;

def score_tweet(line, scores):
    tweets = json.loads(line).get('text', '');
    return sum(scores.get(word, 0) for word in tweets.split());

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = built_score(sent_file);
    for line in tweet_file:
        print "%.1f" % score_tweet(line, scores);

if __name__ == '__main__':
    main()
