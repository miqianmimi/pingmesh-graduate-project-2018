import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket
host = socket.gethostname()
print (host)
sender='miqianmimi@outlook.com'
receivers=['miqianmimi@outlook.com']



message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject='Python SMTP 邮件测试'
message['subject']= Header(subject,'utf-8')


try:
    print(1)
    smtpObj=smtplib.SMTP(host,25)
    print(1)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print(1)
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e)

