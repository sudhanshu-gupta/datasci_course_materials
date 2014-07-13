#!/usr/bin/python

from __future__ import division
import sys
import json

__author__ = 'sudhanshu.gupta'

def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f};

def score_tweet(tweet, scores):
    return (sum(scores.get(word, 0) for word in tweet));

def score_unknown_words(tweet_file, scores):
    with open(tweet_file) as f:
        tweets = (json.loads(line).get('text', '').split() for line in f);
        return {word: score_tweet(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores};


if __name__ == "__main__":
    sent_file = sys.argv[1];
    tweet_file = sys.argv[2];
    scores = read_scores(sent_file);
    sys.stdout.writelines("{0} {1}\n".format(word.encode('utf-8'), score) for word, score in score_unknown_words(tweet_file, scores).items());