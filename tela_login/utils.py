import os
import hashlib
import json
import time


def remove_espaco(string):
    string = string.replace(' ','')
    return string

def procura_caminho(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    return caminho

def leitura_json(nome_arquivo):
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
        with open(caminho, 'r', encoding = 'utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados

def copiar_json(nome_arquivo, nome_backup):
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
        caminho_backup = os.path.join(os.path.dirname(__file__), nome_backup)
        dados = leitura_json(caminho)
        with open(caminho_backup, 'w', encoding = 'utf-8') as backup:
                json.dump(dados, backup, indent=4)

def criptografa_senha(senha):

    #/ Chamada quando necessario criptografar uma senha, ou ate mesmo outra coisa, criptografa e devolve qualquer entrada criptografada.

    cripografada = hashlib.sha256(senha.encode('utf-8'))
    senha_criptografada = cripografada.hexdigest()
    return senha_criptografada

def listar_usuarios(menu):
    #/ Pega usuario por usuario e imprime na tela.
    dados = leitura_json('dados.json')

    for dado in dados:
        print(f'-{dado['login']}')

    input('Pressione enter para retornar')
    time.sleep(1)
    menu()

def limpar_tela():

    #/ limpa a tela e coloca tracejados para o visual mais bonitinho

    os.system('cls')
    print('--------------------------------------------------')

def voltar_menu(menu):
    print('--------------------------------------------------')
    input('Aperte ENTER para retornar ao menu.')
    print('--------------------------------------------------')
    menu()

def fechar():

    #/ encerra o sistema

    limpar_tela()
    return 0

if __name__ == '__main__':
    pass
