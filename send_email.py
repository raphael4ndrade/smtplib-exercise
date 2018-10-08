import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print ('Starting application ...')

toaddr = fromaddr = 'email@gmail.com'
password = 'apppassword'

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
