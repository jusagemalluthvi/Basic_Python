import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Ini adalah percobaan mengirim email melalui python disertai dengan lampiran
'''
#The mail addresses and password
sender_address = 'labu.ekspresif@gmail.com'
sender_pass = 'labuituenak'
receiver_address1 = 'jusagemal.luthvi@gmail.com'
receiver_address2 = 'gemal.gembul@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address1
message['To'] = receiver_address2
message['Subject'] = 'Percobaan 2'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
filename = 'Basic Python #1.pdf'
attach_file = open("E:\jusa\Basic_Python\materi\Basic Python #1.pdf", 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Disposition', "attachment; filename= %s" % filename)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, (receiver_address1, receiver_address2), text)
session.quit()
print('Mail Sent')
