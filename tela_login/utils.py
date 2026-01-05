import os
import hashlib
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def trocar_senha_adm():
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
        print('senha alterada com sucesso')
    else: print('Insira um usuario existente')

def trocar_senha_validacao():
    copiar_json('dados.json', 'backup.json')
    dados = leitura_json('dados.json')
    endereco = procura_caminho('dados.json')

    senha_trocada = False

    usuario = input('informe o nome de usuario: ')
    
    valida_pergunta = valida_resposta(usuario)

    if valida_pergunta:
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
            print('Senha alterada com sucesso')

    else: print('Insira um usuario existente')

def valida_resposta(usuario):
    dados = leitura_json('dados.json')
    for dado in dados:
        if usuario == dado['login']:
            resposta = input(dado['pergunta'])
            if resposta == dado['resposta']:
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

    #/ Chamada quando necessario criptografar uma senha, ou ate mesmo outra coisa, criptografa e devolve qualquer entrada criptografada.

    cripografada = hashlib.sha256(senha.encode('utf-8'))
    criptografada = cripografada.hexdigest()
    return criptografada

def speed_cast(arquivo, adm):
    dados = leitura_json(arquivo)
    caminho = procura_caminho(arquivo)

    usuario = input('Informe o nome do usuario: ')
    usuario = remove_espaco(usuario)

    senha = input('Informe a senha do usuario: ')
    senha = remove_espaco(senha)
    senha = criptografa(senha)

    for dado in dados:
        if dado['login'] == usuario:
            print('este usuario ja existe.')

    novo_usuario = {'login': usuario, 'senha': senha, 'adm': adm}
    dados.append(novo_usuario)

    with open(caminho, 'w', encoding='utf-8' ) as folder:
        json.dump(dados, folder, indent=4)

    return usuario

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

def fechar():

    #/ encerra o sistema

    limpar_tela()
    return 0

if __name__ == '__main__':
    pass
