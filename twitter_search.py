#!/usr/bin/python

def getTweets(query):
    from urllib import urlopen
    from bs4 import BeautifulSoup

    url = 'https://twitter.com/search?f=realtime&q=%s&src=typd' % query
    source = BeautifulSoup(urlopen(url).read(), 'html.parser')
    tweets = []
    for tweet in source.select('.stream-container .content'):
        data = {}
        data['timestamp'] = tweet.select('.tweet-timestamp')[0].attrs['title']
        data['name'] = tweet.select('.fullname')[0].text
        data['content'] = tweet.select('.tweet-text')[0].text
        tweets += [data]
    return tweets
