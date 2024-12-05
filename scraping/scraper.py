import requests
from bs4 import BeautifulSoup

def extrair_conteudo(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        sopa = BeautifulSoup(resposta.text, 'html.parser')

        titulo = sopa.find('h1').get_text(strip=True)
        paragrafos = sopa.find_all('p')
        conteudo = '\n'.join(p.get_text(strip=True) for p in paragrafos)

        return titulo, conteudo
    except Exception as e:
        return None, f"Erro ao extrair conteúdo: {e}"
