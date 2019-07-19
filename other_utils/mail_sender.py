#coding: utf-8  
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'xxxx@126.com'
receiver = 'xxxx@126.com'
subject = 'XX日报'
smtpserver = 'smtp.126.com'
username = '****'
password = '****'

msg = MIMEText('Python 邮件发送这是我们的日报信息...', 'plain', 'utf-8')
msg['Subject'] = Header( subject, 'utf-8' )
msg['From'] = sender
msg['To'] = receiver
smtp = smtplib.SMTP()
smtp.connect( smtpserver )
smtp.login( username, password )
smtp.sendmail( sender, receiver, msg.as_string() )
smtp.quit()