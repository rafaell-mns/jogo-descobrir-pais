import pprint
import random
import requests

def requisicao():
    link = 'https://servicodados.ibge.gov.br/api/v1/paises/{paises}'
    
    try:
        requisicao  = requests.get(link)
        return requisicao.json() # Retorna as informações em formato json
    except Exception as err:
        print(f'Erro na requisição: {err}')
        return None

def seleciona_pais(paises):
    numero_sorteado = random.randint(0, 272)
    
    dados_pais = paises[numero_sorteado]
    
    # exibir os dados json de forma organizada:
    # pprint.pprint(dados_pais)

    nome_pais = dados_pais['nome']['abreviado']
    descricao = dados_pais['historico']
    localizacao = dados_pais['localizacao'] 
    moeda = dados_pais['unidades-monetarias'][0]['nome']

    return nome_pais, descricao, localizacao, moeda