#!/usr/bin/python

def sendMarkdown(text, subject='Message from your agent'):
    import mailer
    from markdown import markdown
    from settings import general

    msg = mailer.Message(From=general['mail_agent'], To=general['mail_notifications'])
    msg.Subject = subject
    msg.Html = markdown(text)
    mailer.Mailer(general['mail_server']).send(msg)
