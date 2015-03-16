#!/usr/bin/python
# coding: utf-8

from time import time
from twitter_search import getTweets
from mail import sendMarkdown
from settings import sources
import simpledb

now = time()
tweetdb = simpledb.read('twitter_report')
if tweetdb is None:
    tweetdb = {'tweets_seen': {}}

new_tweets = []
for term in sources['twitter']['searchTerms']:
    for tweet in getTweets(term):
        content = tweet['content']
        if content not in tweetdb['tweets_seen']:
            new_tweets += [tweet]
        tweetdb['tweets_seen'][content] = now

for content, timestamp in tweetdb['tweets_seen'].items():
    if timestamp + 7 * 24 * 3600 < now:
        del tweetdb['tweets_seen'][content]

simpledb.write('twitter_report', tweetdb)


if len(new_tweets) > 0:
    text = u""
    for tweet in new_tweets:
        text += u"{timestamp}, {name}:\n\n    {content}\n\n".format(**tweet)
    sendMarkdown(text, subject="News from Twitter")
