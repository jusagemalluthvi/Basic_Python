#ref https://poopcode.com/python-code-snippet-how-to-send-doc-smtp/
#ref https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
#ref https://pynative.com/python-accept-list-input-from-user/
#ref https://github.com/FarisNadhila/AI10/blob/main/Final%20Project/Final_Project.py

#import some libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass


#The mail addresses and password
alamat_pengirim = input("{:<40} {:<3}".format("Masukkan email pengirim (nama@gmail.com)", ":"))
pass_pengirim = getpass.getpass("{:<40} {:<3}".format("Masukkan password", ":"))

#Read file that contain email recipients
with open("E:\jusa\Basic_Python\Final-Project\email_penerima.txt", "r") as penerima: 
    daftar_penerima = penerima.read().splitlines()
    print("{:<40} {:<2}".format("List Penerima", ":"), daftar_penerima)

#print(daftar_penerima)
print("=======================================================================================================")
subyek = input("{:<40} {:<3}".format("Masukkan subjek", ":"))
mail_content = input("{:<40} {:<3}".format("Masukkan isi email", ":"))
pilihan = input("{:<40} {:<3}".format("Apakah ada lampiran ? (y/n)", ":"))

if pilihan == 'y':
    attachment = input("{:<40} {:<3}".format("File Location yang ingin dilampirkan", ":"))
    simpan_sebagai = input("{:<40} {:<3}".format("Kirim file dengan nama (nama.ext)", ":"))
    print("=======================================================================================================")

    try:    
        for each_email in daftar_penerima:
            print('Email Sedang Dikirim ke', each_email, " . . . ")
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = alamat_pengirim
            message['To'] = each_email
            message['Subject'] = subyek
            
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            attach_file = open((attachment), 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octet-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) #encode the attachment
            #add payload header with filename
            payload.add_header('Content-Disposition', "attachment; filename= %s" % simpan_sebagai)
            message.attach(payload)
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(alamat_pengirim, pass_pengirim) #login with mail_id and password
            text = message.as_string()
            session.sendmail(alamat_pengirim, each_email, text)
            session.quit()
            print('Email Terkirim')
            print("=======================================================================================================")
    except Exception as gagal:
        print ("Email Gagal Terkirim",gagal)

else :
    print("=======================================================================================================")
    try:    
        for each_email in daftar_penerima:
            print('Email Sedang Dikirim ke', each_email, " . . . ")
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = alamat_pengirim
            message['To'] = each_email
            message['Subject'] = subyek
            
            #The body for the mail
            message.attach(MIMEText(mail_content, 'plain'))

            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(alamat_pengirim, pass_pengirim) #login with mail_id and password
            text = message.as_string()
            session.sendmail(alamat_pengirim, each_email, text)
            session.quit()
            print('Email Terkirim')
            print("=======================================================================================================")
    except Exception as gagal:
        print ("Email Gagal Terkirim",gagal)