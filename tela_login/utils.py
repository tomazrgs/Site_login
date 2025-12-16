import os
import hashlib
import json

from dados import pessoas

def criptografa_lista():
    #/criptografa todas as senhas da lista.

    for pessoa in pessoas:
        if len(pessoa['senha']) != 64: #/ verifica o tamanho da senha, caso seja maior que 64 (tamanho maximo da hash sha256) 
            senha = pessoa['senha']
            cripografada = hashlib.sha256(senha.encode('utf-8'))
            senha_criptografada = cripografada.hexdigest()
            pessoa['senha'] = senha_criptografada

def criptografa_senha(senha):

    #/ Chamada quando necessario criptografar uma senha, ou ate mesmo outra coisa, criptografa e devolve qualquer entrada criptografada.

    cripografada = hashlib.sha256(senha.encode('utf-8'))
    senha_criptografada = cripografada.hexdigest()
    return senha_criptografada

def listar_usuarios(menu):

    #/ Pega usuario por usuario e imprime na tela.

    for pessoa in pessoas:
        print(f'Usuario: {pessoa['login']}')

    input('Pressione qualque tecla para retornar ao menu \n')
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

def leitura_json(nome_arquivo):
    endereco = os.path.join(os.path.dirname(__file__), nome_arquivo)

    with open(endereco, 'r', encoding = 'utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados
    
def copiar_json(nome_arquivo, nome_backup):
    endereco_backup = os.path.join(os.path.dirname(__file__), nome_backup)

    dados = leitura_json(nome_arquivo)
    with open(endereco_backup, 'w', encoding = 'utf-8') as arquivo:
        json.dump(dados, arquivo)


if __name__ == '__main__':
    pass