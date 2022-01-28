#ref https://poopcode.com/python-code-snippet-how-to-send-doc-smtp/
#ref https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
#ref https://pynative.com/python-accept-list-input-from-user/
#ref https://codeinu.com/language/python/c114325-python-send-email-with-attachment
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
            
            message.attach(MIMEText(mail_content, 'plain')) #attach the mail_content to the message instance
            attach_file = open((attachment), 'rb') #open the file as binary mode
            lampiran = MIMEBase('application', 'octet-stream') #instance of MIMEBase and named as lampiran
            lampiran.set_payload((attach_file).read()) #to change the payload into encoded form 
            encoders.encode_base64(lampiran) #encode the attachment           
            lampiran.add_header('Content-Disposition', "attachment; filename= %s" % simpan_sebagai) #add lampiran header with filename
            message.attach(lampiran) #attach the instance 'lampiran' to instance 'message' 
            
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(alamat_pengirim, pass_pengirim) #login with mail_id and password
            text = message.as_string() #converts the Multipart message into a string 
            session.sendmail(alamat_pengirim, each_email, text) #sending the mail 
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
            
            message.attach(MIMEText(mail_content, 'plain')) #attach the mail_content to the message instance

            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(alamat_pengirim, pass_pengirim) #login with mail_id and password
            text = message.as_string() #converts the Multipart message into a string
            session.sendmail(alamat_pengirim, each_email, text) #sending the mail
            session.quit()
            print('Email Terkirim')
            print("=======================================================================================================")
    except Exception as gagal:
        print ("Email Gagal Terkirim",gagal)