import os
import hashlib
import json
import time
import random
import uuid
import string

from tela_login.back.log_config import get_logger

logger = get_logger(__name__)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def codig_seguranca():
    codigo = ''

    while len(codigo) < 6:
        codigo += str(random.randint(0,9))
        codigo += random.choice(string.ascii_letters)
    return codigo
        
def gera_id():
    identifica = str(uuid.uuid4())
    return identifica

def verifica_vazio(string, validacao):
    while string == '':
        string = input(f'Insira um {validacao} valida: ')
        string = remove_espaco(string)
    return string


def valida(correto, informado):
     if correto == informado:
          return True
     else: return False


def remove_espaco(string):
    string_correta = string.replace(' ','')
    return string_correta

def procura_caminho(nome_arquivo):
    global BASE_DIR
    caminho = os.path.join(BASE_DIR, 'data', nome_arquivo)
    return caminho

def leitura_json(nome_arquivo):
        global BASE_DIR
        caminho = os.path.join(BASE_DIR, 'data', nome_arquivo)
        with open(caminho, 'r', encoding = 'utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados

def copiar_json(nome_arquivo, nome_backup):
        global BASE_DIR
        caminho = os.path.join(BASE_DIR, 'data', nome_arquivo)
        caminho_backup = os.path.join(BASE_DIR, 'data', nome_backup)
        dados = leitura_json(caminho)
        with open(caminho_backup, 'w', encoding = 'utf-8') as backup:
                json.dump(dados, backup, indent=4)

def criptografa(senha):

    #/ Chamada quando necessario fazer hash.

    cripografada = hashlib.sha256(senha.encode('utf-8'))
    criptografada = cripografada.hexdigest()
    return criptografada

def listar_usuarios(menu, user):
    #/ Pega usuario por usuario e imprime na tela.
    dados = leitura_json('dados.json')

    for dado in dados:
        print(f'-{dado['login']}')

    input('Pressione enter para retornar')
    logger.info(f'{user} solicitou lista de usuarios.')
    time.sleep(1)
    menu(user)

def limpar_tela():

    #/ limpa a tela e coloca tracejados para o visual mais bonitinho

    os.system('cls')
    print('--------------------------------------------------')

def fechar():

    #/ encerra o sistema

    limpar_tela()
    return 0

if __name__ == '__main__':
    pass
