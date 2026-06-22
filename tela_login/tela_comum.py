import time
import json
import resend

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
from back.utils import trocar_senha_validacao
from back.utils import verifica_vazio

logger = get_logger(__name__)

# resend.api_key = 're_2gzD2hqG_8dvjR4gaT2TcyABTkPpMGZtG'

contas = Contas()

def entrar():
    global contas

    x = 0

    logado = False

    while x < 3 and not logado:

        try:
            dados = leitura_json('dados.json')
        except:
            FileNotFoundError
            logger.error('Arquivo não esta conseguindo ser leito.')
            opcoes()

        for dado in dados:
            dado = Usuario.from_dict(dado)
            contas.adduser(dado)

        usuario = input('Informe seu usuario: ').lower() 
        usuario = remove_espaco(usuario)
        usuario = verifica_vazio(usuario, 'usuario')

        senha = input(f'Olá {usuario} informe sua senha: ')
        senha = remove_espaco(senha)
        senha = verifica_vazio(senha, 'senha')

        senha_criptografada = criptografa(senha)

        usuario_encontrado = contas.verifica_existencia(usuario)

        valida_adm = contas.informa_role(usuario)

        logado = contas.verifica_login(usuario,senha_criptografada)
        time.sleep(3)

        if not usuario_encontrado:
            x += 1
            logger.warning('tentativa de login, usuario nao encontrado')
            erro_login_cad()
        elif usuario_encontrado and valida_adm == 'adm':
            logado = contas.verifica_login(usuario,senha_criptografada)
            if  logado:
                logger.warning(f'Adm {usuario} logado')
                opcoes_adm(usuario)
        else:
            logado = contas.verifica_login(usuario,senha_criptografada)
            if logado:
                print(f'Seja bem vindo {usuario}')
                time.sleep(2)
                logger.warning(f'{usuario} logou com sucesso')
            else:
                x += 1
                logger.warning(f'tentativa de login do usuario {usuario}, senha incorreta ')
                erro_login_cad()


    if x == 3:
        limpar_tela()

        stile('Limite de tentativas excedidas, tente novamente.')
        escolha = input('Caso tenha esquecido sua senha digite "SIM": ').lower()

        if escolha == 'sim':   

            usuario = input('informe o usuario:')

            usuario_encontrado = contas.verifica_existencia(usuario)

            if usuario_encontrado:

                codigo = codig_seguranca()

                resend.Emails.send({
                    "from": "onboarding@resend.dev",
                    "to": "tomazgoncalvessantos@gmail.com",
                    "subject": "<h1>Recuperação de senha</h1>",
                    "html": f"<p><strong>Seu código de recuperação de senha {codigo} </strong></p>"
                })
            
                trocar_senha_validacao(usuario,codigo)
            else:
                print('Usuario inesistente para solicitação de recuperação de senha')
                time.sleep(1)
                logger.info('Reset de senha falhou, usuario inexistente.')
                opcoes()

            logger.info(f'Reset de senha requisitado para usuario: {usuario}.')
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
        dado = Usuario.from_dict(dado)
        contas.adduser(dado)

    i = 0  

    limpar_tela()

    usuario = input('Escolha um nome de usuario: \n').lower()
    usuario = remove_espaco(usuario)

    existe = contas.verifica_existencia(usuario)

    while existe and i < 3:
        usuario = input('Nome de usuario invalido: ')
        i += 1
    if i == 3:
        print('Tentativas excedidas, por favor tente novamente do menu')
        logger.warning('tentativas de cadastro excedidas.')
        time.sleep(2)
        opcoes()

    senha = input('Insira a senha: ') 
    senha = verifica_vazio(senha,'senha')

    repet_senha = input('Digite a senha novamente: ')
    repet_senha = verifica_vazio(repet_senha, 'senha')

    y = 0

    while repet_senha != senha and y < 3:
        y += 1
        repet_senha = input('As senhas são diferentes, por favor digite a mesma senha: ')
        repet_senha = verifica_vazio(senha, 'senha')
    if y == 3:
        print('tentativas excedidas, por favor tente novamente')
        logger.warning('tentativas de cadastro excedidas.')
        time.sleep(2)
        opcoes()

    senha_criptografada = criptografa(senha)

    identifica = gera_id()

    novo_user = Usuario(identifica,usuario,senha_criptografada)

    try:
        dados.append(novo_user.to_dict())

        with open(endereco, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)

        print(f'{usuario} seu cadastro foi feito com sucesso!! ')
        logger.info(f'Novo usuario {usuario} cadastrado.')
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
