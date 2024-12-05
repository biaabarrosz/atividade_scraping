from scraping.scraper import extrair_conteudo
from email_service.sender import enviar_email
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

URL = 'https://www.cnnbrasil.com.br/tecnologia/gatos-sao-liquidos-phd-em-fisica-viraliza-com-estudos-que-dizem-que-sim/'

if __name__ == "__main__":
    titulo, conteudo = extrair_conteudo(URL)
    if titulo:
        enviar_email(titulo, conteudo, EMAIL_REMETENTE, EMAIL_SENHA, DESTINATARIO)
    else:
        print(conteudo)
