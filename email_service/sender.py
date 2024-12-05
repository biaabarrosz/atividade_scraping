import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_email(assunto, corpo, remetente, senha, destinatario):
    try:
        mensagem = MIMEMultipart()
        mensagem['From'] = remetente
        mensagem['To'] = destinatario
        mensagem['Subject'] = assunto

        mensagem.attach(MIMEText(corpo, 'plain'))

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(mensagem)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    enviar_email(
        "Teste de Assunto",
        "Corpo do e-mail para teste",
        os.getenv("EMAIL_REMETENTE"),
        os.getenv("EMAIL_SENHA"),
        os.getenv("EMAIL_DESTINATARIO")
    )
