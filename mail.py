#!/usr/bin/python

def sendHtml(text, subject='Message from your agent'):
    import mailer
    from markdown import markdown
    from settings import general

    msg = mailer.Message(
            From=general['mail_agent'],
            To=general['mail_notifications'],
            charset='utf-8')
    msg.Subject = subject
    msg.Html = text.encode('utf-8')
    mailer.Mailer(general['mail_server']).send(msg)

def sendMarkdown(text, subject='Message from your agent'):
    from markdown import markdown
    sendHtml(markdown(text), subject)
