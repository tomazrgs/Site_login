import time
import json
import resend
import os

from flask import Flask, request, render_template

from dotenv import load_dotenv

from manipula.usuario import Usuario
from manipula.usuario import Contas

from back.log_config import get_logger

from back.tela_adm import opcoes_adm

from back.interface import menu
from back.interface import erro_login_cad
from back.interface import erro_arquivo
from back.interface import stile

from back.utils import codig_seguranca
from back.utils import gera_id
from back.utils import criptografa
from back.utils import limpar_tela
from back.utils import fechar
from back.utils import listar_usuarios
from back.utils import remove_espaco
from back.utils import leitura_json
from back.utils import copiar_json
from back.utils import procura_caminho
from back.utils import verifica_vazio
from back.utils import valida
from back.utils import email_senha
from back.utils import get_ip

logger = get_logger(__name__)
load_dotenv()

app = Flask(__name__)

resend.api_key = os.getenv('api_key')

contas = Contas()

@app.route('/')
def entrar():
    global contas

    x = 0

    logado = False

    while x < 3 and not logado:

        try:
            dados = leitura_json('dados.json')
        except FileNotFoundError as erro:
            logger.error(f'{erro}')
            opcoes()

        for dado in dados:
            dado = Usuario.from_dict(dado)
            contas.adduser(dado)

        usuario = input('Informe seu usuario: ').lower() 
        usuario = remove_espaco(usuario)
        usuario_tratado = verifica_vazio(usuario, 'usuario')

        senha = input(f'Olá {usuario_tratado} informe sua senha: ')
        senha = remove_espaco(senha)
        senha_tratada = verifica_vazio(senha, 'senha')

        senha_hash = criptografa(senha_tratada)

        usuario_encontrado = contas.verifica_existencia(usuario_tratado)

        if usuario_encontrado:
            logado = contas.verifica_login(usuario_tratado,senha_hash)
        # else:
        #     x += 1
        #     logger.warning('tentativa de login, usuario nao encontrado')
        #     erro_login_cad()

        valida_role = contas.informa_role(usuario_tratado)

        if valida_role == 'adm' and logado:
            logger.info(f'Adm {usuario_tratado} logado')
            opcoes_adm(usuario_tratado)
        elif logado:
            print(f'Seja bem vindo {usuario_tratado}')
            time.sleep(2)
            logger.info(f'{usuario_tratado} logou com sucesso')
        else:
            x += 1 
            erro_login_cad()


    if x == 3:
        limpar_tela()

        stile('Limite de tentativas excedidas, tente novamente.')
        logger.warn(f'Computador {get_ip()} excedeu o numero de tentativas')

        escolha = input('Caso tenha esquecido sua senha digite "SIM": ').lower()



        if escolha == 'sim':   

            logger.warn(f'Computador {get_ip()} slicitou troca de senha')

            usuario = input('informe o usuario:')

            usuario_encontrado = contas.verifica_existencia(usuario)

            if usuario_encontrado:

                codigo = email_senha()
                
                codigo_infomado = input('Informe o código de verificação enviado a seu email:')

                codigo_infomado = valida(codigo_infomado,codigo)

                if codigo_infomado:
                    nova_senha = input ("informe uma nova senha: ")
                    objeto = contas.coleta_objeto(usuario)
                    objeto.troca_senha(objeto, nova_senha)
            else:
                print('Usuario inesistente para solicitação de recuperação de senha')
                time.sleep(1)
                opcoes()

            logger.info(f'Reset de senha requisitado para {get_ip()}')
            time.sleep(1)
            opcoes()    

def cadastrar():
    global contas

    try:
        dados = leitura_json('dados.json')
    except:
        logger.error('Arquivo não esta conseguindo ser leito.')
        erro_arquivo()
        opcoes()
    
    copiar_json('dados.json', 'backup.json')

    endereco = procura_caminho('dados.json')

    for dado in dados:
        user = Usuario.from_dict(dado)
        contas.adduser(user)

    limpar_tela()

    usuario = input('Escolha um nome de usuario: \n').lower()
    usuario_tratado = verifica_vazio(remove_espaco(usuario), 'usuario')


    existe = contas.verifica_existencia(usuario_tratado)

    i = 0
    while existe and i < 3:
        usuario = input('Nome de usuario invalido: ')
        usuario_tratado = verifica_vazio(remove_espaco(usuario), 'usuario')
        i += 1
    if i == 3:
        print('Tentativas excedidas, por favor tente novamente do menu')
        logger.warning('tentativas de cadastro excedidas.')
        time.sleep(2)
        opcoes()

    senha = input('Insira a senha: ') 
    senha_tratada = verifica_vazio(remove_espaco(senha),'senha')

    repet_senha = input('Digite a senha novamente: ')
    repet_senha_tratada = verifica_vazio(remove_espaco(repet_senha), 'senha')

    y = 0
    while repet_senha_tratada != senha_tratada and y < 3:   
        repet_senha = input('As senhas são diferentes, por favor digite a mesma senha: ')
        repet_senha_tratada = verifica_vazio(remove_espaco(repet_senha), 'senha')
        y += 1

    if y == 3:
        print('tentativas excedidas, por favor tente novamente')
        logger.warning('tentativas de cadastro excedidas.')
        time.sleep(2)
        opcoes()

    senha_hash = criptografa(senha_tratada)

    identifica = gera_id()

    novo_user = Usuario(identifica,usuario_tratado,senha_hash)

    try:
        dados.append(novo_user.to_dict())

        with open(endereco, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)

        print(f'{usuario_tratado} seu cadastro foi feito com sucesso!! ')
        logger.info(f'Novo usuario {usuario_tratado} cadastrado.')
    except:
        ProcessLookupError

    time.sleep(2)
    opcoes()

def opcoes(): 
    menu()
    #/ lieralmente switch case do C
    try:
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
    except:
        ValueError
        time.sleep(1)
        logger.error('Erro ao escolher opção.')
       
if __name__ == '__main__':
    opcoes()
