#!/usr/bin/python

import os
import mailer
import yaml
from markdown import markdown

settings = yaml.load(open(os.path.expanduser("~/agents_settings/general.yaml")).read())
msg = mailer.Message(From=settings['mail_agent'], To=settings['mail_notifications'])
msg.Subject = "Message"
msg.Html = markdown("""
## Good Morning!

This is a test message.""")
mailer.Mailer(settings['mail_server']).send(msg)
