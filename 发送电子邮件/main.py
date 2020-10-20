import os.path
from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)
app.config.update(
    #EMAIL SETTINGS 
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = '704690152',
    MAIL_PASSWORD = 'ozjzvddayzdgbeej')

def sendEmail(From, To, Subject, Body, Html, Attachments):
    '''To：必须是 list'''
    msg=Message(Subject, sender=From, recipients=To)
    msg.body=Body
    msg.html=Html
    with app.open_resource(Attachments) as fp:
        msg.attach(filename=os.path.basename(Attachments),
                   data=fp.read(),
                   content_type='application/octet-stream')
    mail=Mail(app)
    with app.app_context():
        mail.send(msg)

if __name__=='__main__':
    From='704690152@qq.com'
    To=['2015167872@qq.com']
    Subject='hello'
    Body='Only a text'
    Html='<h1>test</h1>'
    Attachments='D:\\FFOutput\\附件.txt'
    sendEmail(From, To, Subject, Body, Html, Attachments)