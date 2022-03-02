from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Email:
    def __init__(self, destinatarios: str, usuario: str, senha: str, ) -> None:
        """Instancia a classe com as configurações iniciais para enviar email
        Args:
            destinatario (str): email do destinatario
            usuario (str): email do usuario
            senha (str): senha do email do usuario
        """

        self.fromaddr = usuario
        self.toaddr = destinatarios
        self.password = senha

    def enviar_email(self):
        """Função responsável por enviar o email.
        Ela anexa um arquivo pptx no email e envia o email para varios destinatarios.
        """
        print('fazendo login')
        print('***'*20)
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.fromaddr, self.password)

            print('anexando arquivo')
            print('***'*20)
            filename = "Workmap.pptx"
            anexo = open("Apresentação Talentos.pptx", "rb")

            p = MIMEBase('aplication', 'octet-stream')
            p.set_payload((anexo).read())
            encoders.encode_base64(p)
            p.add_header("Content-Disposition",
                         "attachment; filename= %s" % filename)

            for email in self.toaddr:
                print(f"Escrevendo email para {email}")
                print('***'*20)
                msg = MIMEMultipart()
                msg['From'] = self.fromaddr
                msg['To'] = email

                # Assunto do email
                msg['Subject'] = "Bem vindo ao time GOE"
                # Corpo do emial

                body = f'''
                <p><b>Olá!</b><br>
                        
                        Seja muito bem-vindo(a) ao time GOE.
                        <br>
                        Segue em anexo o nosso Workmap para você conhecer melhor
                        como trabalhamos.
                        </p>'''
                msg.attach(MIMEText(body, 'html'))
                msg.attach(p)

                text = msg.as_string()
                print('enviando')
                smtp.sendmail(msg['From'], msg['To'], text)
                print('Email enviado com sucesso!')
                print('***'*20)

        sair = ''
        while sair != 'x':
            sair = input(
                "Envio de Emails finalizado, digite x para sair: ")
