import time
import json

from tela_login.log_config import get_logger

from tela_login.tela_adm import opcoes_adm

from data.org import Usuario
from data.org import Contas

from tela_login.interface import menu
from tela_login.interface import erro_login_cad
from tela_login.interface import erro_arquivo
from tela_login.interface import stile


from tela_login.utils import gera_id
from tela_login.utils import criptografa
from tela_login.utils import limpar_tela
from tela_login.utils import fechar
from tela_login.utils import listar_usuarios
from tela_login.utils import remove_espaco
from tela_login.utils import leitura_json
from tela_login.utils import copiar_json
from tela_login.utils import procura_caminho
from tela_login.utils import trocar_senha_validacao
from tela_login.utils import verifica_vazio

logger = get_logger(__name__)
contas = Contas()


def entrar():
    global contas
    global logger

    x = 0

    usuario_encontrado = False

    while x < 3 or not usuario_encontrado:

        try:
            dados = leitura_json('dados.json')
        except:
            erro_arquivo()
            logger.error('Arquivo não esta conseguindo ser leito.')
            opcoes()

        usuario = input('Informe seu usuario: ').lower() 
        usuario = remove_espaco(usuario)
        usuario = verifica_vazio(usuario, 'usuario')

        senha = input(f'Olá {usuario} informe sua senha: ')
        senha = remove_espaco(senha)
        senha = verifica_vazio(senha, 'senha')

        senha_criptografada = criptografa(senha)

        contas.adduser(dados)

        verifica = contas.verifi_login(usuario,senha_criptografada)

        adm = contas.verifi_adm(usuario)

        if verifica:
            print(f'{usuario} logado com sucesso')

            logger.info(f'{usuario} logado com sucesso')

            usuario_encontrado == True
            
            if adm:
                logger.info(f'{usuario} foi logado como adm.')
                
                opcoes_adm(usuario)

                # increment_pergunta(usuario)
        elif not verifica:
            x += 1
            logger.warning('tentativa de login, usuario nao encontrado')
            erro_login_cad()
            
    if x == 3:
        limpar_tela()

        stile('Limite de tentativas excedidas, tente novamente.')
        escolha = input('Caso tenha esquecido sua senha digite "SIM": ').lower()

        if escolha == 'sim':
            logger.info('Reset de senha requisitado.')
            trocar_senha_validacao()
            time.sleep(1)
            opcoes()

def cadastrar():
    global contas
    global logger

    try:
        dados = leitura_json('dados.json')
    except:
        logger.error('Arquivo não esta conseguindo ser leito.')
        erro_arquivo()
        opcoes()
        
    copiar_json('dados.json', 'backup.json')
    endereco = procura_caminho('dados.json')

    for dado in dados:
        contas.adduser(Usuario.from_dict(dado))

    i = 0

    limpar_tela()
    usuario = input('Escolha um nome de usuario: \n').lower()
    usuario = verifica_vazio(usuario, 'usuario')
    
    valida = contas.verifi_exist(usuario)

    print(valida)

    while usuario == '' or valida:
        usuario = input('Usuario invalido, por favor tente outro: ')
        i += 1
        if i == 3:
            print('Tentativas excedidas, por favor tente novamente do menu')
            logger.warning('tentativas de cadastro excedidas.')
            time.sleep(2)
            opcoes()

    senha = input('Insira a senha: ')
    senha = remove_espaco(senha) 

    while senha == '': 
        print('Senha invalida por favor tente novamente\n')
        senha = input('Crie uma senha: ')
        senha = remove_espaco(senha)

    senha_criptografada = criptografa(senha)

    repet_senha = input('Digite a senha novamente:')
    repet_senha = remove_espaco(senha)

    y = 0

    while repet_senha != senha and y < 3:
        y += 1
        repet_senha = input('As senhas são diferentes, por favor digite a mesma senha:')
        repet_senha = remove_espaco(senha)
    if y == 3:
        print('tentativas excedidas, por favor tente novamente')
        logger.warning('tentativas de cadastro excedidas.')
        time.sleep(2)
        opcoes()

    identifica = gera_id()

    novo_usuario = Usuario(identifica, usuario,senha_criptografada)

    dados.append(novo_usuario.to_dict())

    with open(endereco, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4)

    print(f'{usuario} seu cadastro foi feito com sucesso!! ')
    logger.info(f'Novo usuario {usuario} cadastrado.')
    time.sleep(2)
    opcoes()

def opcoes(): 
    menu()
    #/ lieralmente switch case do C

    escolha = int(input('\nEscolha uma opção: '))
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
    opcoes()
