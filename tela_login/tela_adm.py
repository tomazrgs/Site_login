import time
import json
import logging

from log_config import get_logger

from interface import menu_admin
from interface import erro_arquivo

from utils import limpar_tela
from utils import listar_usuarios
from utils import fechar
from utils import copiar_json
from utils import leitura_json
from utils import procura_caminho
from utils import remove_espaco
from utils import procura_caminho
from utils import speed_cast
from utils import trocar_senha_adm

logger = get_logger(__name__)

def promocao_adm(user):
    caminho = procura_caminho('dados,json')
    dados = leitura_json('dados.json')
    novo_adm = input ('Informe o nome do usuario: ')
    novo_adm = remove_espaco(novo_adm)
    

    for dado in dados:
        if dado['login'] == novo_adm and dado['adm'] == False:
            dado['adm'] = True

            try:
                with open(caminho,'w', encoding='utf-8') as arquivo:
                    json.dump(dados,arquivo, indent=4)
            except:
                erro_arquivo()
                logger.error('Arquivo não esta conseguindo ser leito.')
                opcoes_adm()

            print(f'{novo_adm} agora é um adm')
            logger.info(f'{user} promoveu {novo_adm} a ADM.')

        elif dado['login'] == novo_adm and dado['adm']:
            print('usuario já é um adm')
            logger.warning(f'{user} tentou promover {novo_adm} mas já é um ADM.')
            time.sleep(2)
            opcoes_adm()

def cad_adm(user):
    caminho = procura_caminho('dados.json')
    novo_adm = speed_cast('dados.json', True)
    dados = leitura_json('dados.json')
    logger.info(f'{user} realizou o cadastro de {novo_adm}')

    try:
        with open(caminho,'w', encoding='utf-8') as arquivo:
            json.dump(dados,arquivo, indent=4)
    except:
        erro_arquivo()
        logger.error('Arquivo impossibilitado de abrir ou ser achado.')
        opcoes_adm()

    print(f'{novo_adm} cadastrado como adm')
    opcoes_adm(user)

def opcao_novo_adm(escolha, user):

    match escolha:
        case 1:
            promocao_adm(user)
        case 2:
            cad_adm(user)

def novo_admin(user):

    limpar_tela()

    print('1: Usuario existente\n' \
          '2: Usuario não existente\n')
    escolha = int(input('Escolha uma opção: '))
    opcao_novo_adm(escolha, user)

def deletar_usuario(user):
    dados = leitura_json('dados.json')
    copiar_json('dados.json', 'backup.json')
    caminho = procura_caminho('dados.json')

    usuario = input('Informe o usuario que deseja deletar: ')

    for indice, dado in enumerate(dados):
        if usuario == dado['login']:
            dados.pop(indice)

    with open(caminho, 'w', encoding='utf') as folder:
        json.dump(dados,folder, indent=4)

    logger.info(f'O ADM {user} deletou a conta de {usuario}')

def opcoes_adm(user):
    #/ lieralmente switch case do C
    menu_admin()

    escolha = int(input('\nEscolha uma opção '))
    match escolha:
        case 1: # Chama a função entrar
            novo_admin(user)
        case 2:
            trocar_senha_adm(user)
        case 3:
            deletar_usuario(user)
        case 4:
            listar_usuarios(opcoes_adm, user)
        case 5:
            fechar()

if __name__ == '__main__':
    pass
