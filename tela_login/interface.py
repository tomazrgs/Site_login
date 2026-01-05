import time


from utils import limpar_tela

def erro_arquivo():
    FileNotFoundError
    limpar_tela()
    print('--------------------------------------------------')
    print('Arquivo não encontrado')
    print('--------------------------------------------------')
    time.sleep(2)

def voltar_menu(menu):
    print('--------------------------------------------------')
    input('Aperte ENTER para retornar ao menu.')
    print('--------------------------------------------------')
    menu()

def menu():

    limpar_tela()
    print('\n1: Entrar ' 
    '\n2: Cadastrar' 
    '\n3: Lista de usuários'
    '\n4: Sair') 
    print('--------------------------------------------------')

def menu_admin():

    limpar_tela()
    print('--bem vindo ao menu de adm--')
    
    print('\n1: Cadastrar outro adm ' 
    '\n2: Trocar senha de usuario' 
    '\n3: Remover Usuario'
    '\n4: Listar usuários'
    '\n5: Sair') 
    print('--------------------------------------------------')

def erro_login_cad():
    print('Usuario ou senha invalidos por favor tete novamente.')
    time.sleep(2)
    
if __name__ == '__main__':
    pass
