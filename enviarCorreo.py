import smtplib

from email.mime.text import MIMEText
msg=MTMEText("Contenido de correo")

msg['subject']='Asunto del correo'
msg['From']='desdedonde@gmail.com'
msg['To']='haciadonde@gmail.com'


mailServer=smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('joseluis@gmail.com',"contraseña")
mailServer.snedmail('joseluis@gmail.com', 'joseluis@gmail.com', msf_as_string("cositas"))

mailServer.close()
