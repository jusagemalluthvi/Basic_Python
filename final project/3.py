import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = ' Ini adalah percobaan mengirim email melalui python disertai dengan lampiran '

#The mail addresses and password
sender_address = 'labu.ekspresif@gmail.com'
sender_pass = 'labuituenak'
receiver = input("Masukkan email penerima (pisah dengan spasi) : ")
print("\n")
receiver_address = receiver.split()
print("List penerima : ", receiver_address)
print("\n")

for recipient in receiver_address:
    try:
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = recipient
        message['Subject'] = 'Percobaan mengirim attachment'
        #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file = open("D:\JUSA\watermark-KTP.png", 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('content-disposition', 'attachment', filename='ktp.png')
        message.attach(payload)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, recipient, text)
        session.quit()
        print('Email Terkirim')

    except Exception as ex:
        print ("Gagal",ex)