#!/usr/bin/python

from __future__ import division
import json
import sys
from collections import defaultdict

__author__ = 'sudhanshu.gupta'

def read_scores(score_file):
    with open(score_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f};

def score_tweet(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet.split());

def parse_tweet(tweet):
    try:
        country = tweet['place']['country_code'];
        state = tweet['place']['full_name'].split(', ')[1];
        text = tweet['text'];
        return country, state, text
    except (KeyError, IndexError, TypeError):
        return None;

def happiest_states(tweet_file, sent_scores):
    n_tweet, scores, happiness = [defaultdict(float) for _ in range(3)];
    with open(tweet_file) as f:
        tweets = (json.loads(line) for line in f);
        parsed_tweets = (parse_tweet(tweet) for tweet in tweets if parse_tweet(tweet));
        state_scores = ((state, score_tweet(tweet=text, scores=sent_scores)) for country, state, text in parsed_tweets if len(state) == 2 and country == "US");

        for state, score in state_scores:
            n_tweet[state] += 1;
            scores[state] += score;
            happiness[state] = scores[state] / n_tweet[state];
    return max(happiness, key=happiness.get);

if __name__ == "__main__":
    sent_scores=read_scores(score_file=sys.argv[1])
    print (happiest_states(tweet_file=sys.argv[2], sent_scores=sent_scores));
