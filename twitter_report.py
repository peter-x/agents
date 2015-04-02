#!/usr/bin/python
# coding: utf-8

from time import time
from twitter_search import getTweets
from mail import sendHtml
from cgi import escape
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

def formatContent(c):
    from re import sub
    c = escape(c)
    return sub(ur"(https?://[a-zA-Z0-9!$&()*+:/?#\[\]@,:='\~.-_]*)", ur'<a href="\1">\1</a>', c)

if len(new_tweets) > 0:
    text = ur'<html><meta charset="utf-8">'
    text += ur'<body style="width: 50ex; font: 16px/1.6 &quot;Helvetica Neue&quot;,Helvetica,Arial,freesans,sans-serif;">'
    for tweet in new_tweets:
        tweet['timestamp'] = escape(tweet['timestamp'])
        tweet['name'] = escape(tweet['name'])
        tweet['content'] = formatContent(tweet['content'])
        text += u"<h4>{timestamp}, {name}</h4><p>{content}</p>\n".format(**tweet)
    text += u'</body></html>'
    sendHtml(text, subject="News from Twitter")
