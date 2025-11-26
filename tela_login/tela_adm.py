
from tela_comum import pessoas
from tela_comum import criptografa_senha

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