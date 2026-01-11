import time
import json

from interface import menu_admin

from utils import criptografa
from utils import limpar_tela
from utils import listar_usuarios
from utils import fechar
from utils import copiar_json
from utils import leitura_json
from utils import procura_caminho
from utils import remove_espaco
from utils import procura_caminho
from utils import speed_cast
from utils import trocar_senha_adm

    
def novo_admin():
    encontrado = None
    caminho = procura_caminho('dados.json')
    limpar_tela()

    print('1: Usuario existente\n' \
        '2: Usuario não existente\n')

    escolha = int(input('Escolha uma opção: '))

    match escolha:
        case 1:
            dados = leitura_json('dados.json')
            novo_adm = input ('Informe o nome do usuario: ')
            novo_adm = remove_espaco(novo_adm)

            for dado in dados:
                if dado['login'] == novo_adm and dado['adm'] == False:
                    encontrado = True
                    dado['adm'] = True
                    print(f'{novo_adm} agora é um adm')

                elif dado['login'] == novo_adm and dado['adm']:
                    print('usuario já é um adm')
                    time.sleep(2)
                    opcoes_adm()
        case 2:
            novo_adm = speed_cast('dados.json', False)
            dados = leitura_json('dados.json')
            for dado in dados:
                if dado['login'] == novo_adm and dado['adm'] == False:
                    encontrado = True
                    dado['adm'] = True
                    print(f'{novo_adm} cadastrado como adm')

    if encontrado:
        with open(caminho,'w', encoding='utf-8') as arquivo:
            json.dump(dados,arquivo, indent=4)

def deletar_usuario():
    dados = leitura_json('dados.json')
    copiar_json('dados.json', 'backup.json')
    caminho = procura_caminho('dados.json')

    usuario = input('Informe o usuario que deseja deletar: ')

    for indice, dado in enumerate(dados):
        if usuario == dado['login']:
            dados.pop(indice)

    with open(caminho, 'w', encoding='utf') as folder:
        json.dump(dados,folder, indent=4)

def opcoes_adm():
    #/ lieralmente switch case do C
    menu_admin()

    escolha = int(input('\nEscolha uma opção '))
    match escolha:
        case 1: # Chama a função entrar
            novo_admin()
        case 2:
            trocar_senha_adm()
        case 3:
            deletar_usuario()
        case 4:
            listar_usuarios(opcoes_adm)
        case 5:
            fechar()

if __name__ == '__main__':
    pass
