import time
import json


from manipula.usuario import Contas
from manipula.usuario import Usuario

from back.log_config import get_logger

from back.interface import menu_admin
from back.interface import erro_arquivo

from back.utils import limpar_tela
from back.utils import listar_usuarios
from back.utils import fechar
from back.utils import copiar_json
from back.utils import leitura_json
from back.utils import procura_caminho
from back.utils import remove_espaco
from back.utils import procura_caminho
from back.utils import criptografa

logger = get_logger(__name__)
contas = Contas()


def promocao_adm(adm): #verificar função, mexendo diretamente com json, tentar adicionar funcões na classe que façam a função ter menos responsabilidade;
    global contas

    try:
        caminho = procura_caminho('dados,json')
        dados = leitura_json('dados.json')
    except:
        FileNotFoundError

    novo_adm = input ('Informe o nome de usuario: ')
    novo_adm = remove_espaco(novo_adm)

    try:
        if Usuario.promover(novo_adm):
            try:
                with open(caminho,'w', encoding='utf-8') as arquivo:
                    json.dump(dados,arquivo, indent=4)
            except:
                FileExistsError
                logger.error('Arquivo não esta conseguindo ser leito.')
                opcoes_adm()

                print(f'{novo_adm} agora é um adm')
                logger.info(f'{adm} promoveu {novo_adm} a ADM.')

        elif not contas.verifica_existencia:
            print('usuario inexiste.')
            logger.warning(f'{adm} tentou promover {novo_adm} mas este usuario é enexistente em nosso banco de dados.')
            time.sleep(1)
            opcoes_adm()

        else:
            print('usuario já é um adm')
            logger.warning(f'{adm} tentou promover {novo_adm} mas já é um ADM.')
            time.sleep(2)
            opcoes_adm()
    except:
        PermissionError

# def novo_admin(adm):

#     limpar_tela()
#     try:
#         print('1: Usuario existente\n'
#             '2: Usuario não existente\n')
#         escolha = int(input('Escolha uma opção: '))

#         match escolha:
#             case 1:
#                 promocao_adm(adm)
#             case 2:
#                 cad_adm(user)

#     except:
#         ValueError
#         logger.info(f'o adm {adm} selecionou um numero invalido ou adicionou letras, na seção de criação de novo adm.')

def deletar_usuario(adm):
    carrega = ''
    i = 0
    try:
        dados = leitura_json('dados.json')
        copiar_json('dados.json', 'backup.json')
        caminho = procura_caminho('dados.json')
    except:
        FileNotFoundError
        logger.warning(f'Arquivo não consegue ser encontrado')
        print('Arquivo não encontrado')
        time.sleep(0.5)
        opcoes_adm()

    usuario = input('Informe o usuario que deseja deletar: ')
    
    while len(carrega) < 10:
        limpar_tela()
        i += 10
        carrega += '|'
        percent = f'- {i}%'
        print(carrega,percent)
        time.sleep(0.5)
        
    print('1 - sim \n' 
        '2- não')
    escolha = input(f'Deseja deletar  {usuario}?')
    
    if escolha == 1:
        for indice, dado in enumerate(dados):
            if usuario == dado['login']:
                dados.pop(indice)
                
        try:
            with open(caminho, 'w', encoding='utf') as folder:
                json.dump(dados,folder, indent=4)
        except:
            FileNotFoundError
            logger.warning(f'Documento não encontrado')
            logger.info(f'O ADM {adm} tentou deletar a conta de {usuario}')

        logger.info(f'O ADM {adm} deletou a conta de {usuario}')

def trocar_senha_adm(adm): # Verificar sobre algumas verificações e loops
    senha_trocada = False

    try:
        copiar_json('dados.json', 'backup.json')
        dados = leitura_json('dados.json')
        endereco = procura_caminho('dados.json')
    except:
        FileNotFoundError
        logger.info('Arquivo não encontrado')

    usuario = input('informe o nome de usuario: ')

    for dado in dados:
        if usuario == dado['login']:
            nova_senha = input('Digite a nova senha: ')
            nova_senha = remove_espaco(nova_senha)
            senha_criptografada = criptografa(nova_senha)
            dado['senha'] = senha_criptografada
            senha_trocada = True

    if  senha_trocada:
        with open(endereco, 'w', encoding= 'utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)
        logger.info(f'{adm} trocou a senha de {usuario}.')
        print('senha alterada com sucesso')
    else: print('Insira um usuario existente')

    return 0


def opcoes_adm(adm):
    #/ lieralmente switch case do C
    menu_admin()

    try:

        escolha = int(input('\nEscolha uma opção '))
        match escolha:
            case 1: # Chama a função entrar
                promocao_adm(adm)
            case 2:
                trocar_senha_adm(adm)
            case 3:
                deletar_usuario(adm)
            case 4:
                listar_usuarios(opcoes_adm, adm)
            case 5:
                fechar()
    except:
        ValueError
        logger.info(f'{adm} colocou numero invalido ou letras, na seção do menu.')

if __name__ == '__main__':
    pass
