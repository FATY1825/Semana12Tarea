from os import getenv
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional
 

class Correo:
    def __init__(self):
        self.Server= SMTP(
            host=getenv("SMTP_HOSTNAME"),
            hoste=getenv("SMTP_PORT")
        )

    def conectar_server(self):
        self.Server.starttls()
        self.Server.login(
            user=getenv("SMTP_USER"),
            password=getenv("SMTP_PASSWORD")
        )

    def mandar_correo(self,email:List[str],contenido:Optional[str], **kwargs):
        self.conectar_server()
        for destn in email:
            mime = MIMEMultipart()
            mime['From']=getenv("STMP_USER")
            mime['To']=destn
            mime['Subject']=contenido
            format = MIMEText(kwargs['message_format'], kwargs['format'])
            mime.attach(format)
            self.Server.sendmail(getenv("STMP_USER"),destn,mime.as_string())
            self.desconectar_server()


    def desconectar_server(self):
        self.Server.quit()
        self.Server.close

