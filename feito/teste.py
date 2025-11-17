from pathlib import Path
import json

caminho = Path('feito').absolute()


def verificar_json(arquivo):
    try:
        with open(fr'{caminho}\{arquivo}', 'r'):
            pass
    except FileNotFoundError:
        with open(fr'{caminho}\{arquivo}', 'a') as f:
            f.write('{}')
            pass


def salvar_jogo(nome, turno, tab1, tab2, tab_de_jogo1, tab_de_jogo2=0, clean_list=0):

    # Modo JxJ
    if type(tab_de_jogo2) != list:

        verificar_json('jj_mode.json')
        with open(fr'{caminho}\jj_mode.json', 'r') as jj_save:
            dados = json.load(jj_save)

        dados[nome] = {
            'tab1': tab1,
            'tab2': tab2,
            'tab_de_jogo1': tab_de_jogo1,
            'tab_de_jogo2': tab_de_jogo2,
            'turno': turno
        }

        with open(fr'{caminho}\jj_mode.json', 'w') as jj_save:
            json.dump(dados, jj_save, indent=4)


    # Modo Jogador x Máquina
    else:

        verificar_json('jm_mode.json')
        with open(fr'{caminho}\jm_mode.json', 'r') as jm_save:
            dados = json.load(jj_save)

        dados[nome] = {
            'tab1': tab1,
            'tab2': tab2,
            'tab_de_jogo': tab_de_jogo1,
            'clean_list': clean_list,
            'turno': turno
        }

        with open(fr'{caminho}\jm_mode.json', 'w') as jm_save:
            json.dump(dados, jm_save, indent=4)


def carregar_jogo(nome, tipo):

    if tipo == 2:
        if Path(fr'{caminho}\jj_mode.json').exists():

            with open(fr'{caminho}\jj_mode.json', 'r') as jj_save:
                dados = json.load(jj_save)
                
            if nome in dados:
                tab1 = dados[nome]['tab1']
                tab2 = dados[nome]['tab2']
                tab_de_jogo1 = dados[nome]['tab_de_jogo1']
                tab_de_jogo2 = dados[nome]['tab_de_jogo2']
                turno = dados[nome]['turno']
                
                fase2(tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)

            else:
                print('\nNão há nenhum jogo salvo!')
                input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
                os.system('cls')
    
        else:
                print('\nNão há nenhum jogo salvo!')
                input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
                os.system('cls')

    else:
        if Path(fr'{caminho}\jm_mode.json').exists():

            with open(fr'{caminho}\jm_mode.json', 'r') as jm_save:
                dados = json.load(jm_save)
                
            if nome in dados:
                tab1 = dados[nome]['tab1']
                tab2 = dados[nome]['tab2']
                tab_de_jogo = dados[nome]['tab_de_jogo']
                clean_list = dados[nome]['clean_list']
                turno = dados[nome]['turno']
                
                fase2(tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)

            else:
                print('\nNão há nenhum jogo salvo!')
                input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
                os.system('cls')

        else:
                print('\nNão há nenhum jogo salvo!')
                input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
                os.system('cls')