import time
import json

from utils import criptografa_senha
from utils import limpar_tela
from utils import voltar_menu
from utils import fechar
from utils import listar_usuarios
from utils import remove_espaco
from utils import leitura_json
from utils import copiar_json
from utils import procura_caminho

def entrar():
    x = 0

    while x < 3:
        usuario_encontrado = False
        dados = leitura_json('dados.json')

        usuario = input('Informe seu usuario: ').lower() 
        usuario = remove_espaco(usuario)

        while usuario == '':
            usuario = input('Escreva nome de usuario: ')
            usuario = remove_espaco(usuario)

        senha = input(f'Olá {usuario} informe sua senha: ')
        senha_criptografada = criptografa_senha(senha)

        for dado in dados:
            if dado['login'] == usuario and dado['senha'] == senha_criptografada:
                usuario_encontrado = True
                print('logado com sucesso')
                break

        if not usuario_encontrado:
            x += 1
            print('Usuario ou senha invalidos, por favor tente novamente:')
            time.sleep(1)
            

    if x == 3:
        print('Limite de tentativas excedidas, tente novamente.')
        time.sleep(2)
        voltar_menu(menu)

def cadastrar():
    dados = leitura_json('dados.json')
    copiar_json('dados.json', 'backup.json')

    i = 0 

    usuario = input('Escolha um nome de usuario: \n')
    usuario = remove_espaco(usuario)
    endereco = procura_caminho('dados.json')

    for dado in dados:
        while dado['login'] == usuario or usuario == '':
            usuario = input('Usuario invalido, por favor tente outro: ')
            i += 1
            if i == 3:
                print('Tentativas excedidas, por favor tente novamente do menu')
                time.sleep(2)
                voltar_menu(menu)

    senha = input('Insira a senha: ')
    senha = remove_espaco(senha) 

    while senha == '': 

        print('Senha invalida por favor tente novamente\n')
        senha = input('Crie uma senha: ')
        senha = remove_espaco(senha)

    senha_criptografada = criptografa_senha(senha)

    repet_senha = input('Digite a senha novamente:')
    repet_senha = remove_espaco(senha)

    y =0

    while repet_senha != senha and y < 3:
        y += 1
        repet_senha = input('As senhas são diferentes, por favor digite a mesma senha:')
        repet_senha = remove_espaco(senha)
    if y == 3:
        print('tentativas excedidas, por favor tente novamente')
        time.sleep(2)

    novo_usuario = {'login': usuario , 'senha': senha_criptografada, 'adm': False}

    with open(endereco, 'w', encoding='utf-8') as file:
        dados.append(novo_usuario)
        json.dump(dados, file, indent=4)

    print(f'{usuario} seu cadastro foi feito com sucesso!! ')
    time.sleep(2)
    voltar_menu(menu)

def menu():

    limpar_tela()
    print('\n1: Entrar ' 
    '\n2: Cadastrar' 
    '\n3: Lista de usuários'
    '\n4: Sair') 
    print('--------------------------------------------------')
    opcoes()

def opcoes(): 

    #/ lieralmente switch case do C

    escolha = int(input('\nEscolha uma opção '))
    match escolha:
        case 1: # Chama a função entrar
            entrar()
        case 2: # Chama a função cadastrar
           cadastrar()
        case 3: # Chama a função listar_usuarios
            listar_usuarios(menu)
        case 4: # Chama a função fechar
            fechar()

if __name__ == '__main__':
    menu()
