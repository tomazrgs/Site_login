from dados import pessoas
from utils import criptografa_senha
from utils import limpar_tela



def menu_adim():

    limpar_tela()
    print('\n1: Trocar senha de usuario ' 
    '\n2: Cadastrar outro adm' 
    '\n3: Lista de usuários'
    '\n4: Sair') 
    print('--------------------------------------------------')
    opcoes()

def trocar_senha():
    print('---------------------------')
    usuario = input('Por favor digite o usuario no qual deseja trocar a senha: ')
    
    login_encontrado = None
    for pessoa in pessoas:
        if pessoa['login'] == usuario:
            login_encontrado = pessoa

            nova_senha = input('Digite a nova senha: ')
            senha_criptografada = criptografa_senha(nova_senha)
            
            login_encontrado['senha'] = senha_criptografada

def opcoes():
    #/ lieralmente switch case do C

    escolha = int(input('\nEscolha uma opção '))
    match escolha:
        case 1: # Chama a função entrar
            trocar_senha()

if __name__ == '__main__':
    pass