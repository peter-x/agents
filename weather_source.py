#!/usr/bin/python

def getForecast():
    from urllib import urlopen
    from bs4 import BeautifulSoup

    from settings import sources

    url = 'http://www.wetterspiegel.de/%s.html' % sources['weather']
    source = BeautifulSoup(urlopen(url).read(), 'html.parser')
    data = [{}, {}, {}]
    for i in range(3):
        data[i]['temp_max'] = float(source.find_all(text='max')[i].parent()[1].text.split()[0])
        data[i]['temp_min'] = float(source.find_all(text='min')[i].parent()[1].text.split()[0])
        data[i]['precip'] = float(source.find_all(text='Niederschlag')[i].parent.parent()[0].text.split()[0])
        data[i]['condition'] = source.find_all(text='min')[i].parent.parent.parent.parent.find_all(attrs={'class': 'contentwhite'})[i].text

    return data
