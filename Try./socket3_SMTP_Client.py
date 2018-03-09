from socket import *
heloCommand ='Hello Alice\r\n'
mailserver='www.miqianmimi.com'
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,25))
recvconnect=clientSocket.recv(1024)

print (recvconnect)

if recvconnect[:3]!='220':
    print('220 reply not received from server.')

print('Sending First HELO')
clientSocket.send(heloCommand)
recvhelo=clientSocket.recv(1024)

print (recvhelo)
if recvhelo[:3]!='250':
    print('250 reply not received from server.')

#Send AUTH command and print server response.
print ("Sending AUTH Command")
#AUTH with base64 encoded user name password
clientSocket.send("AUTH PLAIN AG15ZW1haWxAZ21haWwuY29tAG15cGFzc3dvcmQ=\r\n")
recv2 = clientSocket.recv(1024)
print (recv2)
if recv2[:3] != '250':
	print ('250 reply not received from server.')

# Send MAIL FROM command and print server response.
print("Sending MAIL FROM Command")
clientSocket.send("MAIL From: sanghvi.harshit@gmail.com\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
    print (   '250 reply not received from server.')

# Send RCPT TO command and print server response.
print("Sending RCPT TO Command")
clientSocket.send("RCPT TO: hs2619@gmail.com\r\n")
recv2 = clientSocket.recv(1024)
print
recv2
if recv2[:3] != '250':
    print
    '250 reply not received from server.'

# Send DATA command and print server response.
print
"Sending DATA Command"
clientSocket.send("DATA\r\n")
recv2 = clientSocket.recv(1024)
print
recv2
if recv2[:3] != '250':
    print
    '250 reply not received from server.'

# Send Data and print server response.
print
"Sending Data"
clientSocket.send("SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test\n.\n\r\n")
recv2 = clientSocket.recv(1024)
print
recv2
if recv2[:3] != '250':
    print
    '250 reply not received from server.'

# Send QUIT and print server response.
print("Sending QUIT")
clientSocket.send("QUIT\r\n")
recv2 = clientSocket.recv(1024)
print
recv2
if recv2[:3] != '250':
    print('250 reply not received from server.')

print("Mail Sent")

#Using Python SMTP Library
#!/usr/bin/python
import smtplib
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
sender = 'sanghvi.harshit@gmail.com'
password = "password"
recipient = 'hs2619@nyu.edu'
subject = 'SMTP Mail Client Test'
body = "SMTP Mail Client Test"
print("Sending e-mail")
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()

