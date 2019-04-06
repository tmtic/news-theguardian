# coding: utf-8

from os import system # Importar o método system da biblioteca os
from time import sleep # Importar o método sleep da biblioteca time
from requests import get # Importar o método get da biblioteca requests
import json # Importar a biblioteca JSON
import pandas as pd # Importar biblioteca pandas - referindo ao pandas com pd

# Função onde contém o menu para a seleção do tipo de exportação do arquivo, passando como argumento o valor da variavel dados
def menu(dados):

    opcao = 4 # Iniciar variavel opção com o valor diferente de 0, pois 0 é a condição de parada
    
    while opcao != 0:
        try:
            opcao = int(input("""
    1 - Buscar esportes
    2 - Buscar noticias
    3 - Buscar arts
    4 - Buscar todas as noticias
    0 - Sair do programa

        Valor >> """))

        except Exception as erro: # Mostra uma mensagem e informa exceção que ocorreu
            print('Informe um valor válido!', erro)

        if opcao == 1: # Caso a opção seja 1 chama a função buscar_sport()
            buscar_sport(dados)
        elif opcao == 2: # Caso a opção seja 2 chama a função buscar_news()
            buscar_news(dados)
        elif opcao == 3: # Caso a opção seja 3 chama a função buscar_arts()
            buscar_arts(dados)
        elif opcao == 4: # Caso a opção seja 4 chama a função buscar_noticas(), seria todas as noticias encontradas
            buscar_noticias(dados)
        elif opcao == 0:
            print('\n\tObrigado por utilizar o programa!')
        else:
            print('Por favor, digite números entre 0 e 4')

        if opcao in [1234]:
            print("Buscando informações das notícias...")
            sleep(2) # Aguarda 2 segundo antes de passar para próxima instrução

# Função para exportar arquivo CSV
def exportar_csv(titulo, link, nome):
    # Criar o DataFrame para formar a tabela 
    df = pd.DataFrame({'Titulo': titulo, 'Link': link})

    # Importar para CSV
    df.to_csv('%s.csv' %nome, encoding='utf-8-sig' ,index=False, sep=',')
    print('Gerando arquivo...\n')
    sleep(2)
    print("Exportado com sucesso!")

# Função buscar noticias gerais
def buscar_noticias(dados):

    # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    titulo = []
    link = []

    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    for noticia in dados["response"]["results"]:
        titulo.append(noticia["webTitle"])
        link.append(noticia["webUrl"])

    # Codição para verificar se a lista contem algum conteudo
    if len(titulo) == 0:
        print('Não foi encontrado nenhum post encontrado. Tente mais tarde!')
    else:
        # Chamada da função exportar_csv, passando 
        exportar_csv(titulo, link, 'noticias')   

# Função buscar noticias relacionados a esporte
def buscar_sport(dados):
    # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    titulo = []
    link = []

    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    for noticia in dados["response"]["results"]:
        if noticia['pillarName'] == 'Sport':
            titulo.append(noticia["webTitle"])
            link.append(noticia["webUrl"])

    # Codição para verificar se a lista contem algum conteudo
    if len(titulo) == 0:
        print('Não foi encontrado nenhum post referente a esportes. Tente mais tarde!')
    else:
        # Chamada da função exportar_csv, passando 
        exportar_csv(titulo, link, 'sports')

# Função buscar apenas a categoria noticias
def buscar_news(dados):
        # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    titulo = []
    link = []

    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    for noticia in dados["response"]["results"]:
        if noticia['pillarName'] == 'News':
            titulo.append(noticia["webTitle"])
            link.append(noticia["webUrl"])

    # Codição para verificar se a lista contem algum conteudo
    if len(titulo) == 0:
        print('Não foi encontrado nenhum post referente a news. Tente mais tarde!')
    else:
        # Chamada da função exportar_csv, passando 
        exportar_csv(titulo, link, 'news')

# Função buscar noticias relacionadas a artes
def buscar_arts(dados):
    # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    titulo = []
    link = []

    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    for noticia in dados["response"]["results"]:
        if noticia['pillarName'] == 'Arts':
            titulo.append(noticia["webTitle"])
            link.append(noticia["webUrl"])
    
    # Codição para verificar se a lista contem algum conteudo
    if len(titulo) == 0:
        print('Não foi encontrado nenhum post referente a artes. Tente mais tarde!')
    else:
        # Chamada da função exportar_csv, passando 
        exportar_csv(titulo, link, 'arts')

# Função para consultar a API do The Jornal Guardian
def consultar_api():
    
    # Realizar a consulta a API do guardian e armazenar na variável URL
    url = 'https://content.guardianapis.com/search?api-key=49ea9a11-be8c-4103-9ee0-02e66afbf026'

    # Usando o método GET da biblioteca JSON, iremos pegar o conteúdo bruto e jogar na variavel RESPOSTA
    resposta = get(url)

    # Testa se o código de retorno foi 200
    if resposta.status_code == 200:
        print('Acessando a base de dados...')

        # Caso o código de retorno foi 200, obteve sucesso, então iremos pegar os dados e tratar
        dados = resposta.json()
    return dados
      
# Função main, a função principal do código
def main():

    system("cls") # Limpar a tela antes de mostrar o resultado

    # Chamar a função consultar_api e armazenando na variável dados
    dados = consultar_api()

    # Chamada da função menu passando como parametro a variavel dados que contém o valor retornado da função consultar API
    menu(dados)

""" O bloco abaixo só será executado se o script for executado via linha de comando,
    caso você faça um import desse arquivo, essas instruções não serão executadas """
if __name__ == '__main__':
    # Chamada da função main()
    main()