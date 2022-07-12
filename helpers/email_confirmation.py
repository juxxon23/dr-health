"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from helpers.prvdrs import Prvdrs

prv = Prvdrs()

class EmailConfirmation():
    # Credentials
    provider = prv.opt('outlook')
    sender = 'dr.health.quindio@outlook.com'
    password = 'naturalezasalvaje'
    port = 587

    def credentials(self, provider, sender, password, port):
        self.provider = prv.opt(provider)
        self.sender = sender
        self.password = password
        self.port = port

    def send_msg(self, user_mail):
        # Server connection
        server = smtplib.SMTP(self.provider, self.port)
        server.starttls()
        server.ehlo()
        # Authentication
        server.login(self.sender, self.password)
        # message
        message = '<b>Gracias por elegirnos</b>, los servicios de <b>Dr. Health</b> estan disponibles para ti.<br>'
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html'))
        msg['From'] = self.sender
        msg['To'] = user_mail
        msg['Subject'] = 'Registro Exitoso'
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return 'complete'
"""