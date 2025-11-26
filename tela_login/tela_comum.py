import os
import hashlib

pessoas = [{'login':'indeed','senha': '1234', 'adm': False},
           {'login':'fernanda0','senha': 'africa', 'adm': False},
           {'login': 'adm', 'senha': 'adm123', 'adm': True}]


def criptografa_lista():
    #/criptografa todas as senhas da lista.

    for pessoa in pessoas:
        senha = pessoa['senha']
        cripografada = hashlib.sha256(senha.encode('utf-8'))
        senha_criptografada = cripografada.hexdigest()
        pessoa['senha'] = senha_criptografada

def criptografa_senha(senha):

    #/ Chamada quando necessario criptografar uma senha, ou ate mesmo outra coisa, criptografa e devolve qualquer entrada criptografada.

    cripografada = hashlib.sha256(senha.encode('utf-8'))
    senha_criptografada = cripografada.hexdigest()
    return senha_criptografada

def voltar_menu():
    #/ returona ao menu ao pressionar qualquer tecla
    input('')
    menu()

def fechar():

    #/ encerra o sistema

    limpar_tela()
    return 0

def limpar_tela():

    #/ limpa a tela e coloca tracejados para o visual mais bonitinho

    os.system('cls')
    print('--------------------------------------------------')

def entrar():
    limpar_tela()

    #/ .lower() força todas os caracteres do input a ficarem minusculos.

    usuario = input('Informe seu usuario: ').lower() 

    #/ Valida se o nome digitado a cima realmente existe dentro do dicionário pessoas.
    login_encontrado = None

    for pessoa in pessoas:
        if pessoa['login'] == usuario:
            login_encontrado = pessoa #/ aqui, foi usado if para armazenar a posição do usuario desejado, para quando for comparar a senha ele compare a senha do usuario correto.
            break
        
    #/Valida se a senha digitada realmente condiz com a senha exata do usuario na lista.
    #/Caso senha ou usuario estejam errados, exibira uma mensagem e puxara o menu novamente 

    if login_encontrado == None:
        input('Usuario não encontrado, tente novamente')
        menu()

    senha = input(f'Olá {usuario} informe sua senha: ')

    senha_criptografada = criptografa_senha(senha)

    if login_encontrado['senha'] ==  senha_criptografada:
        limpar_tela()
        print('----LOGADO COM SUCESSO----')

        if login_encontrado['adm']:
            print('bem vindo ao menu de adm!!')

    else:
        input('Usuario ou senha invalida, tente novamente.')
        menu()

    
def cadastrar():

    i = 0 #/ iniciamos a variavel i para utiliza-la em uma validação a baixo, sempre que for incrementar uma variavel é necessário inicialização, por ser int não podemos utilizar None.
    usuario = input('Escolha um nome de usuario: \n')
    usuario = usuario.replace(' ','') #/ Troca espaços por areas vazias para a validação a baixo.

    while usuario == '':
        print('Usuario invalido, por favor informe um usuario DECENTE \n')
        usuario = input('Informe outro usuario: ')
        usuario = usuario.replace(' ','') #/ Troca espaços por areas vazias.

    #/ Compara o usuario digitado no dicionário de pessoas, para não existir usuários iguais.
    #/ Tem um limite de 3 (tres) tentativas, caso permaneça colocando usuarios existentes, sera levado ao menu.
    #/ O problema em adicionar limite de tentativas foi resolvido com o primeiro IF, apenas pedindo para incrementar i.

    for pessoa in pessoas:
        if pessoa['login'] == usuario:
            print('Este usuário já existe por favor informe outro: ')
            i += 1
            if i == 3:
                input('Tentativas excedidas, por favor tente novamente do menu')
                menu()

    #/ Ao solicitar a criação da senha, tive um desafio, como impedir que o usuario coloque apenas espaço ou apenas de ENTER no input.

    senha = input('Crie uma senha: ')
    senha = senha.replace(' ','') #/ O desafio foi resolvido fácilmente utilizando replace, um tempo depois adicionei replace a cina para validar o usuario também.

    while senha == '': #/ Utilizei while para que 'enquanto a senha tiver apenas enter ou espaço', ele entrara no laço e pedira uma senha até ser da forma correta.
        print('Senha invalida por favor tente novamente\n')
        senha = input('Crie uma senha: ')
        senha = senha.replace(' ','')

    #/ Criptografa a senha utilizando MD5 e formata logo em baixo para ser exibida apenas em exadecimal.

    cripografada = hashlib.md5(senha.encode('utf-8'))
    senha_criptografada = cripografada.hexdigest()

    #/ Solicitamos para que digite novamente a senha, exatamente como foi digitado a cima, para validação.

    repet_senha = input('Digite a senha novamente:')
    repet_senha = repet_senha.replace(' ','')

    while repet_senha != senha: #/ caso seja diferente, peço para redigitar, pensando em adicionar limite de tentativas.
        repet_senha = input('As senhas são diferentes, por favor digite a mesma senha: ')
        repet_senha = repet_senha.replace(' ','')

    #/ Adiciono o usuario novo ao dicionário e exibo uma mensagem de cadastro bem sucedido.

    novo_usuario = {'login': usuario , 'senha': senha, 'adm': False}
    pessoas.append(novo_usuario)
    print(f'{usuario} seu cadastro foi feito com sucesso ')
    menu()

def listar_usuarios():

    #/ Pega usuario por usuario e imprime na tela.

    for pessoa in pessoas:
        print(f'Usuario: {pessoa['login']}')

    input('Pressione qualque tecla para retornar ao menu \n')
    menu()

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
            listar_usuarios()
        case 4: # Chama a função fechar
            fechar()

if __name__ == '__main__':
    criptografa_lista()
    menu()