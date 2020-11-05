from flask_mail import Message
from flask import render_template
from . import mail
from .models import Comments
def mail_message(subject,template,*kwa,**kwargs):

    sender_email="pwambui13@gmail.com"
    emails=Comments.query.all()
    all_emails=[]
    for email in emails:
        all_emails.append(email.email)
    
    if len(all_emails)>0:
        email=Message(subject,sender=sender_email,recipients=all_emails)
        email.body=render_template(template+".txt",**kwargs)
        email.html=render_template(template+".html",**kwargs)

        mail.send(email)
