#!/usr/bin/python
# coding: utf-8

from weather_source import getForecast
from mail import sendMarkdown

forecast = getForecast()

days = ['Heute', 'Morgen', u'Übermorgen']
text = u'## Wettervorhersage\n\n'
for i in range(len(days)):
    data = {'day': days[i]}
    data.update(forecast[i])

    text += u"""
{day}:

- Temperatur: {temp_min:.1f} - {temp_max:.1f}
- Niederschlag: {precip:.1f} mm
- {condition}

""".format(**data)

sendMarkdown(text)
