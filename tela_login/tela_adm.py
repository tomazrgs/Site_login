from dados import pessoas
from utils import criptografa_senha
from utils import limpar_tela
from utils import listar_usuarios
from utils import fechar

def menu_admin():

    limpar_tela()

    print('--bem vindo ao menu de adm--')
    
    print('\n1: Cadastrar outro adm ' 
    '\n2: Trocar senha de usuario' 
    '\n3 Remover Usuario'
    '\n4: Listar usuários'
    '\n5: Sair') 
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

def novo_admin():
    limpar_tela()

    novo_adm = input ('Informe o usuario: ')
    novo_adm = novo_adm.replace(' ','')

    for pessoa in pessoas:
        if pessoa['login'] == novo_adm and pessoa['adm'] == False:

            pessoa['adm'] = True

            print('Usuario promovido a ADM')
            input('Pressione ENTER para retornar ao menu:')
            menu_admin()

        elif pessoa['login'] == novo_adm and pessoa['adm'] == True:
            print('Usuario já é um ADM')
            input('Pressione ENTER para retornar ao menu:')
            menu_admin()

def deletar_usuario():

    usuario = input('Informe o usuario que deseja deletar: ')

    for indice, pessoa in enumerate(pessoas):
        if usuario == pessoa['login']:
            del pessoa[indice]

def opcoes():
    #/ lieralmente switch case do C

    escolha = int(input('\nEscolha uma opção '))
    match escolha:
        case 1: # Chama a função entrar
            novo_admin()
        case 2:
            trocar_senha()
        case 3:
            deletar_usuario()
        case 4:
            listar_usuarios()
        case 5:
            fechar()

if __name__ == '__main__':
    pass
