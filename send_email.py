# The MIME module just is native in python 2.7. Doesn work with python3
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

print ('Starting application ...')

toaddr = fromaddr = 'raphael4ndrade@gmail.com'
password = ''

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Python Report'

body = "testing python script to send an email using smtplib"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text )
server.quit()

print ('Done!')