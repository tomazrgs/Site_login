import os
import hashlib
import json
import time
import random
import uuid
import string

from back.log_config import get_logger

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

def trocar_senha_adm(user):
    copiar_json('dados.json', 'backup.json')
    dados = leitura_json('dados.json')
    endereco = procura_caminho('dados.json')

    senha_trocada = False

    usuario = input('informe o nome de usuario: ')

    for dado in dados:
        if usuario == dado['login']:
            nova_senha = input('Digite a nova senha: ')
            nova_senha = remove_espaco(nova_senha)
            senha_criptografada = criptografa(nova_senha)
            dado['senha'] = senha_criptografada
            senha_trocada = True

    if  senha_trocada:
        with open(endereco, 'w', encoding= 'utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)
        logger.info(f'{user} trocou a senha de {usuario}.')
        print('senha alterada com sucesso')
    else: print('Insira um usuario existente')

def trocar_senha_validacao(usuario ,codigo_enviado):
    try:
        copiar_json('dados.json', 'backup.json')
        dados = leitura_json('dados.json')
        endereco = procura_caminho('dados.json')
    except:
        FileNotFoundError

    limpar_tela()

    codigo_informado = input('informe o código de segurança por favor: ')

    if codigo_informado == codigo_enviado:
        senha = input('Por favor informe uma nova senha: ')
        senha = verifica_vazio(senha, 'senha')

        for dado in dados:
            if dado['login'] == usuario:
                senha = criptografa(senha)
                dado['senha'] = senha
    try:
        with open(endereco, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)
    except:
        FileExistsError

# def valida_resposta(usuario):
#     dados = leitura_json('dados.json')
#     for dado in dados:
#         if usuario == dado['login']:
#             resposta = input(dado['pergunta'])
#             if resposta == dado['resposta']:
#                 return True
#             else: return False
    
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
