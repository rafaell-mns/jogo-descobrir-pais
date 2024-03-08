import re
from functions import *

def exibir_localizacao(localizacao):
    continente = localizacao['regiao']['nome']
    regiao_intermediaria = localizacao.get('regiao-intermediaria')
    continente_especifico = regiao_intermediaria['nome'] if regiao_intermediaria else ''
    sub_regiao = localizacao['sub-regiao']['nome']

    localizacao = f'LOCALIZAÇÃO: {continente}, '
    if continente_especifico:
        localizacao += f'{continente_especifico}, '
    localizacao += f'{sub_regiao}.\n'
    print(localizacao)

def esconder_nome(nome_pais):
    substituido = ""
    for caractere in nome_pais:
        if caractere.isalpha():
            substituido += 'X'
        else:
            substituido += caractere
    return substituido

def exibir_descricao(descricao, nome_pais):
    # Esconder o nome do país
    pais_disfarcado = esconder_nome(nome_pais)
    descricao = descricao.replace(nome_pais, pais_disfarcado)

    # Retirar a fonte no final do texto que revela a resposta
    match = re.search(r'Fonte(s)?:', descricao)
    posicao_fontes = match.start()
    descricao = descricao[:posicao_fontes]

    print("DESCRIÇÃO: " + descricao)

def exibir_dica(nome_pais, moeda):
    primeira_letra = nome_pais[0]
    nome_pais.replace(' ','')

    print(f'\nDICA: O nome do país começa com a letra {primeira_letra} e possui {len(nome_pais)} letras.Sua moeda é o {moeda}.')

def jogar():
    historico = []
    paises = requisicao()

    while True:
        nome_pais, descricao, localizacao, moeda = seleciona_pais(paises)

        print("="*120)
        exibir_localizacao(localizacao)
        exibir_descricao(descricao, nome_pais)
        exibir_dica(nome_pais, moeda)
        print("="*120)

        tentativa = input("Digite sua resposta: ").lower()
        
        mensagem = "\nParabéns!" if tentativa == nome_pais.lower() else f"\nResposta errada.\nResposta certa: {nome_pais}"

        print(mensagem)

        historico.append(nome_pais)

        again = input("\nDeseja jogar de novo? [s/n] ")
        print("")
        if(again != 's'):
            print("Histórico de jogo:")
            for pais in historico:
                print(pais)
            break
    
jogar()