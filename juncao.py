#RECONHECIMENTO DO USUÁRIO
def cadastro(nome, senha):
    cadastros = open('usuarios.txt', 'a')
    cadastros.write(f'{nome};{senha}\n')
    cadastros.close()
    os.system('cls')
    print('\nUsuário cadastrado com sucesso! Por favor, faça login para jogar!\n')

def login(nome, senha):
    cadastros = open('usuarios.txt', 'r')
    conteudo_cadastros = cadastros.read()
    linhas = conteudo_cadastros.split('\n')
    if f'{nome};{senha}' in linhas:
        verificador = True
    else:
        verificador = False
        print('O usuário não pode ser encontrado ou a senha está incorreta. Porfavor tente novamente.')
    cadastros.close()

    return verificador

########################################################################################################################

#TABULEIRO
def gerar_tabuleiro():
    tab = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tab.append(linha)
    return tab

main_tab = gerar_tabuleiro()


def montar_main_tab(tab):
    tab_ = []
    for linhas in range(10):
        linha = ' '.join([
            '🔵' if j == 0 else
            '⬜' if j == 1 else
            '🔳' if j == 2 else
            '❌' if j == -1 else
            str(j) for j in tab[linhas]
            ])
        tab_.append(linha)

    print('  A', '  B', ' C', ' D', ' E', '  F', ' G', ' H', ' I', ' J')
    for linhas in range(10):
        print(linhas,tab_[linhas])


# TAB 0 = tabuleiro para os chutes das casas
tab_0 = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(-1)
    tab_0.append(linha)


def montar_tab_chute(tab):
    tab_ = []
    for linhas in range(10):
        linha = ' '.join([
            '🏳️' if j == 0 else
            '🚩' if j == 1 else
            '🏴' if j == 2 else
            '⏺️' if j == -1 else
            str(j) for j in tab[linhas]
            ])
        tab_.append(linha)
    return tab_

#TAB OCULTO = tabuleiro de chutes VAZIO (-1) montado
tab_oculto = montar_tab_chute(tab_0)

def exibir_tab(tab):
    print('  A', '  B', ' C', ' D', ' E', '  F', ' G', ' H', ' I', ' J')
    for linhas in range(10):
        print(linhas, tab[linhas])

########################################################################################################################

#CARREGAMENTO DE JOGO
from pathlib import Path
import importlib.util
import os
import copy

#Montando o caminho absoluto da pasta de saves de forma idependente ao utilizador
caminho = Path('saves').absolute()
os.makedirs('saves', exist_ok=True)

#Essa função é capaz de importar elementos de outros arquivos .py (utilizada para o carregamento de saves)
def importar_item(caminho, item):
    nome_usuario = os.path.splitext(os.path.basename(caminho))[0]
    spec = importlib.util.spec_from_file_location(nome_usuario, caminho)
    save = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(save)
    return getattr(save, item)



#Fase 1 é a primeira etapa do jogo, onde o jogador distribui seus barcos pelo tabuleiro
def fase1():
    # FASE 1
    player_tab = []
    _tab = main_tab.copy()
    for n in range(2):
        os.system('cls')
        d2 = 0
        c3 = 0
        e4 = 0
        p5 = 1
        while d2 + c3 + e4 + p5 != 0:
            os.system('cls')
            print('')
            print('=' * 50)
            print(f'                    Jogador {n + 1}\n')
            print('=' * 50)
            print('')
            montar_main_tab(_tab)

            print('')
            print('=' * 50)
            print(f'[1]  {d2}x Destróier:🔳⬜\n[2]  {c3}x Cruzador: ⬜🔳⬜\n'
                  f'[3]  {e4}x Encouraçado: ⬜🔳⬜⬜\n[4]  {p5}x Porta-aviões: ⬜⬜🔳⬜⬜')
            print('=' * 50)
            while True:
                peca = input('\nSelecione um navio e sua orientação(v/h)...\n>').lower()
                posicao = input('\nSelecione uma casa...\n>').lower()
                if len(peca) != 2 or not (peca[0].isdigit()) or type(peca) != str:
                    print('Entrada Inválida!')
                    print(1)
                    continue
                elif not(1 <= int(peca[0]) <= 4) or (peca[1] != 'h' and peca[1] != 'v'):
                    print('Entrada Inválida!')
                    print(2)
                    continue

                if posicao[1].isdigit():
                    if not(0 <= int(posicao[1]) <= 9) or not('A' <= posicao[0].upper() <= 'J'):
                        print('Entrada Inválida!')
                        print(3)
                        continue
                elif posicao[0].isdigit():
                    posicao = f'{posicao[1]}{posicao[0]}'
                    if not(0 <= posicao[1] <= 9) or not('A' <= posicao[0] <= 'J'):
                        print('Entrada Inválida!')
                        print(4)
                        continue
                    else:
                        break

                break

            j = ord(posicao[0]) - 97
            i = int(posicao[1])

            match int(peca[0]):
                case 1:
                    if d2 == 0:
                        print('\nVocê não tem mais navios desse tipo!\n')
                        continue
                    elif _tab[i][j] != 0 or _tab[i][j] != 0:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                    elif peca[1] == 'h' and _tab[i][j + 1] == 0:

                        if not (0 <= j < 9):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i][j + 1] = 1
                            _tab[i][j] = 2
                            d2 -= 1

                    elif peca[1] == 'v' and _tab[i + 1][j] == 0:

                        if not (0 <= i < 9):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i + 1][j] = 1
                            _tab[i][j] = 2
                            d2 -= 1

                    else:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                case 2:
                    if c3 == 0:
                        print('\nVocê não tem mais navios desse tipo!\n')
                        continue
                    elif _tab[i][j] != 0 or _tab[i][j] != 0:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                    elif peca[1] == 'h' and _tab[i][j + 1] == 0 and _tab[i][j - 1] == 0:

                        if not (0 < j < 9):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i][j + 1] = 1
                            _tab[i][j - 1] = 1
                            _tab[i][j] = 2
                            c3 -= 1

                    elif peca[1] == 'v' and _tab[i + 1][j] == 0 and _tab[i - 1][j] == 0:

                        if not (0 < i < 9):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i + 1][j] = 1
                            _tab[i - 1][j] = 1
                            _tab[i][j] = 2
                            c3 -= 1

                    else:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                case 3:

                    if e4 == 0:
                        print('\nVocê não tem mais navios desse tipo!\n')
                        continue
                    elif _tab[i][j] != 0 or _tab[i][j] != 0:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                    elif peca[1] == 'h' and _tab[i][j + 1] == 0 and _tab[i][j + 2] == 0 and _tab[i][j - 1] == 0:

                        if not (0 < j < 8):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i][j + 1] = 1
                            _tab[i][j + 2] = 1
                            _tab[i][j - 1] = 1
                            _tab[i][j] = 2
                            e4 -= 1

                    elif peca[1] == 'v' and _tab[i + 1][j] == 0 and _tab[i + 2][j] == 0 and _tab[i - 1][j] == 0:

                        if not (0 < i < 8):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i + 1][j] = 1
                            _tab[i + 2][j] = 1
                            _tab[i - 1][j] = 1
                            _tab[i][j] = 2
                            e4 -= 1

                    else:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                case 4:

                    if p5 == 0:
                        print('\nVocê não tem mais navios desse tipo!\n')
                        continue
                    elif _tab[i][j] != 0 or _tab[i][j] != 0:
                        print('\nEste lugar já está ocupado!\n')
                        continue

                    elif peca[1] == 'h' and _tab[i][j + 1] == 0 and _tab[i][j + 2] == 0 and _tab[i][j - 1] == 0 \
                            and _tab[i][j - 2] == 0:

                        if not (1 < j < 8):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i][j + 1] = 1
                            _tab[i][j + 2] = 1
                            _tab[i][j - 1] = 1
                            _tab[i][j - 2] = 1
                            _tab[i][j] = 2
                            p5 -= 1

                    elif peca[1] == 'v' and _tab[i + 1][j] == 0 and _tab[i + 2][j] == 0 and _tab[i - 1][j] == 0 \
                            and _tab[i - 2][j] == 0:

                        if not (1 < i < 8):
                            print('\nO navio não cabe no local, tente outra casa ou outra orientação!\n')
                            continue
                        else:
                            _tab[i + 1][j] = 1
                            _tab[i + 2][j] = 1
                            _tab[i - 1][j] = 1
                            _tab[i - 2][j] = 1
                            _tab[i][j] = 2
                            p5 -= 1

                    else:
                        print('\nEste lugar já está ocupado!\n')
                        continue

        player_tab.append(_tab.copy())
        _tab = gerar_tabuleiro()
        os.system('cls')
    return player_tab


def salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):
    save_usuario = fr'{str(caminho)}\{nome}.py'
    save = open(save_usuario, 'w')
    save.write(f'tab1 = {tab1}\n'
               f'tab2 = {tab2}\n'
               f'tab_de_jogo1 = {tab_de_jogo1}\n'
               f'tab_de_jogo2 = {tab_de_jogo2}\n'
               f'turno = {turno}')
    save.close()


#A fase 2 é a segunda etapa do jogo, onde os jogadores tentam adivinhar onde o navio inimigo está
def fase2(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):
    os.system('cls')
    # Parametros de ação
    salvamento = 0
    j1 = 0
    j2 = 0

    while True:
        if turno % 2 == 1:
            print('')
            print('=' * 50)
            print(f'                    Jogador 1\n')
            print('=' * 50)
            continuar = int(input('[1] ATACAR\n[2] SALVAR JOGO E SAIR\n> '))
            print('=' * 50)
            match continuar:
                case 1:
                    exibir_tab(montar_tab_chute(tab_de_jogo2))
                    while True:
                        print('')
                        ij = input('Insira as coordenadas para o ataque:\n> ')
                        print('')
                        if ij[0].isdigit():
                            ij = f'{ij[1]}{ij[0]}'
                        if not(0 <= int(ij[1]) <= 9) or not('A' <= ij[0] <= 'J'):
                                print('Entrada Inválida!')
                                continue
                        else:
                            break
                    j = ord(ij[0].lower()) - 97
                    i = int(ij[1])
                    if tab2[i][j] == 0:
                        tab_de_jogo2[i][j] = 0
                        exibir_tab(montar_tab_chute(tab_de_jogo2))
                        print('=' * 50)
                        print('Errou!')
                        print('=' * 50)
                        input(' ')
                        turno += 1
                    elif tab2[i][j] == 1:
                        tab_de_jogo2[i][j] = 1
                        exibir_tab(montar_tab_chute(tab_de_jogo2))
                        print('=' * 50)
                        print('Na mosca! Você acertou uma parte do navio inimigo!')
                        print('=' * 50)
                        input(' ')
                        tab2[i][j] = -1
                    elif tab2[i][j] == 2:
                        tab_de_jogo2[i][j] = 2
                        exibir_tab(montar_tab_chute(tab_de_jogo2))
                        print('=' * 50)
                        print('Em cheio! Você acertou bem no meio do navio inimigo!')
                        print('=' * 50)
                        input(' ')
                        tab2[i][j] = -1
                case 2:
                    salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                    salvamento = 1
                    break

        elif turno % 2 == 0:
            print('')
            print('=' * 50)
            print(f'                    Jogador 2\n')
            print('=' * 50)
            continuar = int(input('[1] ATACAR\n[2] SALVAR JOGO E SAIR\n> '))
            print('=' * 50)
            match continuar:
                case 1:
                    exibir_tab(montar_tab_chute(tab_de_jogo2))
                    while True:
                        print('')
                        ij = input('Insira as coordenadas para o ataque:\n> ')
                        print('')
                        if ij[0].isdigit():
                            ij = f'{ij[1]}{ij[0]}'
                        if not (0 <= int(ij[1]) <= 9) or not ('A' <= ij[0] <= 'J'):
                            print('Entrada Inválida!')
                            continue
                        else:
                            break
                    j = ord(ij[0].lower()) - 97
                    i = int(ij[1])

                    if tab1[i][j] == 0:
                        tab_de_jogo1[i][j] = 0
                        exibir_tab(montar_tab_chute(tab_de_jogo1))
                        print('=' * 50)
                        print('Errou!')
                        print('=' * 50)
                        input(' ')
                        turno += 1
                    elif tab1[i][j] == 1:
                        tab_de_jogo1[i][j] = 1
                        exibir_tab(montar_tab_chute(tab_de_jogo1))
                        print('=' * 50)
                        print('Na mosca! Você acertou uma parte do navio inimigo!')
                        print('=' * 50)
                        input(' ')
                        tab1[i][j] = -1
                    elif tab1[i][j] == 2:
                        tab_de_jogo1[i][j] = 2
                        exibir_tab(montar_tab_chute(tab_de_jogo1))
                        print('=' * 50)
                        print('Em cheio! Você acertou bem no meio do navio inimigo!')
                        print('=' * 50)
                        input(' ')
                        tab1[i][j] = -1
                case 2:
                    salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                    salvamento = 1
                    break

        parametro1 = 0
        parametro2 = 0
        for i in range(10):
            for j in range(10):
                if tab1[i][j] == 1 or tab1[i][j] == 2:
                    parametro1 += 1

                if tab2[i][j] == 1 or tab2[i][j] == 2:
                    parametro2 += 1

        if parametro1 == 0:
            print('=' * 50)
            print('           🏆 O JOGADOR 2 VENCEU!!! 🏆\n')
            print('                   Jogador 2 🥇')
            print('                   Jogador 1 🥈')
            print('=' * 50)
            print('Tabuleiro do Jogador 1🥈\n')
            montar_main_tab(tab1)
            print('=' * 50)
            print('Tabuleiro do Jogador 2🥇\n')
            montar_main_tab(tab2)
            print(' \n' * 2)
            input('Sair...\n> ')
            j2 = 1
            break

        if parametro2 == 0:
            print('=' * 50)
            print('           🏆 O JOGADOR 1 VENCEU!!! 🏆\n')
            print('                   Jogador 1 🥇')
            print('                   Jogador 2 🥈')
            print('=' * 50)
            print('Tabuleiro do Jogador 1🥇\n')
            montar_main_tab(tab1)
            print('=' * 50)
            print('Tabuleiro do Jogador 2🥈\n')
            montar_main_tab(tab2)
            print(' \n' * 2)
            input('Sair...\n> ')
            j1 = 1
            break


def JvsJ(nome):
    player_tab = fase1()
    tab1 = player_tab[0].copy()
    tab2 = player_tab[1].copy()
    fase2(nome, tab1, tab2, copy.deepcopy(tab_0), copy.deepcopy(tab_0), 1)
    menu_login(nome)

#importa os elementos necessários para a continuação do jogo salvo do arquivo .py correspondente de cada jogador.
def carregar_jogo(nome):
    if Path(fr'{str(caminho)}\{nome}.py').exists():
        tab1 = importar_item(fr'{str(caminho)}\{nome}.py', 'tab1')
        tab2 = importar_item(fr'{str(caminho)}\{nome}.py', 'tab2')
        tab_de_jogo1 = importar_item(fr'{str(caminho)}\{nome}.py', 'tab_de_jogo1')
        tab_de_jogo2 = importar_item(fr'{str(caminho)}\{nome}.py', 'tab_de_jogo2')
        turno = importar_item(fr'{str(caminho)}\{nome}.py', 'turno')
        fase2(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
    else:
        print('Não há nenhum jogo salvo!')
        return -1

########################################################################################################################


#MENU PRINCIPAL E DE LOGIN
def menu_login(nome):
    os.system('cls')
    while True:
        print('')
        print('=' * 30)
        print(f'     Seja Bem-Vindo, {nome}!\n')
        print('=' * 30)
        print('1 - Novo Jogo\n2 - Carregar Jogo\n3 - Logout')
        print('=' * 30)
        escolha = int(input('> '))
        match escolha:
            case 1:
                os.system('cls')
                print('')
                print('=' * 30)
                print(f'  Selecione o Modo de Jogo!\n')
                print('=' * 30)
                print('1 - Jogador vs. Máquina\n2 - Jogador vs. Jogador\n3 - Voltar')
                print('=' * 30)
                escolha_ = int(input('> '))
                match escolha_:
                    case 1:
                        ...
                    case 2:
                        JvsJ(nome)
                    case 3:
                        continue
            case 2:
                carregar_jogo(nome)
                os.system('cls')
            case 3:
                main_menu()
                break

def main_menu():
    os.system('cls')
    while True:
        print('=' * 30)
        print('     💣 Batalha Naval 🛳️')
        print('=' * 30)
        print('1 - Fazer Login\n2 - Cadastrar Usuário\n3 - Sair')
        print('=' * 30)
        escolha = int(input('> '))
        match escolha:
            case 1:
                nome = input('\nInsira o nome de usuário: ')
                senha = input('Digite sua senha: ')
                if login(nome,senha):
                    menu_login(nome)
                else:
                    continue
            case 2:
                try:
                    with open('usuarios.txt', 'r'):
                        pass
                except FileNotFoundError:
                    with open('usuarios.txt', 'a'):
                        pass
                nome = input('\nInsira o nome de usuário: ')
                senha = input('Escolha uma senha: ')
                cadastros = open('usuarios.txt', 'r')
                if nome in cadastros.read():
                    print('\nJá existe um usuário com esse nome, por favor tente outro!\n')
                else:
                    cadastro(nome,senha)
                cadastros.close()
                continue
            case 3:
                break
    
    exit()


main_menu()