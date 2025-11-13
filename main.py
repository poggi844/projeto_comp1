# RECONHECIMENTO DO USUÁRIO
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
        input('\nO usuário não pode ser encontrado ou a senha está incorreta. Porfavor tente novamente. ')
    cadastros.close()

    return verificador

#_____________________________________________________________________________________________________________

# TABULEIRO
def gerar_tabuleiro():
    tab = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tab.append(linha)
    return tab
main_tab = gerar_tabuleiro()

# Esta função transforma um tabuleiro de números em um de imagens, para um entendimento visual
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


# Equivalente à função anterior, porém com um tabuleiro de chutes
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


# TAB OCULTO = tabuleiro de chutes VAZIO (-1) montado
tab_oculto = montar_tab_chute(tab_0)


#Exibe o tabuleiro final com um cabeçalho
def exibir_tab(tab):
    print('  A', '  B', ' C', ' D', ' E', '  F', ' G', ' H', ' I', ' J')
    for linhas in range(10):
        print(linhas, tab[linhas])

#_____________________________________________________________________________________________________________

# CARREGAMENTO DE JOGO
from pathlib import Path
import importlib.util, os, copy, random


#Montando o caminho absoluto da pasta de saves de forma idependente ao utilizador
caminho = Path('saves').absolute()


# Garantindo a existencia dos componentes do jogo (diretório "saves" e "usuarios.txt")
try:
    with open('usuarios.txt', 'r'):
        pass
except FileNotFoundError:
    with open('usuarios.txt', 'a'):
        pass

os.makedirs('saves', exist_ok=True)
#--------------------------------------------

# Essa função é capaz de importar elementos de outros arquivos .py (utilizada para o carregamento de saves)
def importar_item(caminho, item):
    nome_usuario = os.path.splitext(os.path.basename(caminho))[0]
    spec = importlib.util.spec_from_file_location(nome_usuario, caminho)
    save = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(save)
    return getattr(save, item)


# Fase 1 é a primeira etapa do jogo, onde o jogador distribui seus barcos pelo tabuleiro
def fase1():

    tabs_montados = [] # Local onde irá ser armazenado os tabuleiros feitos pelos jogadores
    tab_montado = main_tab.copy() # Tabuleiro em que o jogador irá montar o seu próprio em cima do tabuleiro base (main_tab)

    for jogador in range(2): # O código se repete para os dois jogadores

        #os.system('cls') # Limpando o terminal para começar a fase 1
        print('funcao')

        # Quantidades de cada tipo de barco.

        d2 = 0  # Destróier
        c3 = 0  # Cruzador
        e4 = 0  # Encouraçado
        p5 = 1  # Porta-aviões

        while d2 + c3 + e4 + p5 != 0: # O turno do jogador roda até acabar os barcos

            #os.system('cls')
            print('peca') 

            # Cabeçalho da fase
            #-----------------------------------------------------------------------------------
            print('')
            print('=' * 50)
            print(f'                    Jogador {jogador + 1}\n')
            print('=' * 50)
            print('')
            montar_main_tab(tab_montado)
            print('')
            print('=' * 50)
            print(f'[1]  {d2}x Destróier:🔳⬜\n[2]  {c3}x Cruzador: ⬜🔳⬜\n'
                  f'[3]  {e4}x Encouraçado: ⬜🔳⬜⬜\n[4]  {p5}x Porta-aviões: ⬜⬜🔳⬜⬜')
            print('=' * 50)
            #------------------------------------------------------------------------------------


            while True: # Loop para corrigir possíveis erros de entrada

                peca = input('\nSelecione um NAVIO [1, 2, 3 ou 4] e sua ORIENTAÇÃO [H ou V]...\n>').upper().replace(' ', '')
                posicao = input('\nSelecione uma COORDENADA...\n>').upper().replace(' ', '')

                # Verificações da peça
                if peca[1].isdigit():
                    peca = f'{peca[1]}{peca[0]}'

                if len(peca) == 2:
                    if 1 <= int(peca[0]) <= 4 and (peca[1] == 'H' or peca[1] == 'V'):
                        verificacao_peca = True
                    else:
                        verificacao_peca = False
                else:
                    verificacao_peca = False
                
                # Verificações da posição
                if posicao[0].isdigit():
                    posicao = f'{posicao[1]}{posicao[0]}'
                
                if len(posicao) == 2:
                    if 'A' <= posicao[0] <= 'J' and 0 <= int(posicao[1]) <= 9:
                        verificacao_posicao = True
                    else:
                        verificacao_peca = False
                else:
                    verificacao_posicao = False

                
                # Validação de entradas
                if verificacao_peca and verificacao_posicao:
                    break
                else:
                    print('\nEntrada(s) inválida(s)! Se atente a forma devida.\n')
                    input('Pressione qualquer tecla para inserir novas entradas... ')
                    continue


            # Coordenadas, peça e orientação de entrada
            j = ord(posicao[0]) - 65
            i = int(posicao[1])

            barco = int(peca[0])

            if peca[1] == 'H':
                direcao = 1
            elif peca[1] == 'V':
                direcao = 2


            # Agora é a parte chata em que é verificado se a entrada de posicionamento do jogador é válida.
            match barco:
                case 1:
                    if d2 == 0:
                        print('Você não tem mais NAVIOS desse tipo.')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue

                    try:
                        if direcao == 1:
                            if (tab_montado[i][j], tab_montado[i][j+1]) == (0,0):

                                tab_montado[i][j+1] = 1
                                tab_montado[i][j] = 2
                                d2 -= 1
                        
                        elif direcao == 2:
                            if (tab_montado[i][j], tab_montado[i+1][j]) == (0,0):

                                tab_montado[i+1][j] = 1
                                tab_montado[i][j] = 2
                                d2 -= 1

                        else:
                            print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                            input('Pressione qualquer tecla para inserir novas entradas... ')
                            
                        continue

                    except:
                        print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue


                case 2:
                    if c3 == 0:
                        print('Você não tem mais NAVIOS desse tipo.')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue
                    
                    try:
                        if direcao == 1:
                            if (tab_montado[i][j-1], tab_montado[i][j], tab_montado[i][j+1]) == (0,0,0):


                                tab_montado[i][j-1] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i][j+1] = 1
                                c3 -= 1
                    
                        elif direcao == 2:
                            if (tab_montado[i-1][j], tab_montado[i][j], tab_montado[i+1][j]) == (0,0,0):

                                tab_montado[i-1][j] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i+1][j] = 1
                                c3 -= 1

                        else:
                            print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                            input('Pressione qualquer tecla para inserir novas entradas... ')
                            
                        continue

                    except:
                        print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue
                        

                case 3:
                    if e4 == 0:
                        print('Você não tem mais NAVIOS desse tipo.')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue

                    try: 
                        if direcao == 1:
                            if (tab_montado[i][j-1], tab_montado[i][j], tab_montado[i][j+1], tab_montado[i][j+2]) == (0,0,0,0):


                                tab_montado[i][j-1] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i][j+1] = 1
                                tab_montado[i][j+2] = 1
                                e4 -= 1
                        
                        elif direcao == 2:
                            if (tab_montado[i-1][j], tab_montado[i][j], tab_montado[i+1][j], tab_montado[i+2][j]) == (0,0,0,0):

                                tab_montado[i-1][j] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i+1][j] = 1
                                tab_montado[i+2][j]
                                e4 -= 1

                        else:
                            print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                            input('Pressione qualquer tecla para inserir novas entradas... ')
                            
                        continue

                    except:
                        print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue



                case 4:
                    if p5 == 0:
                        print('Você não tem mais NAVIOS desse tipo.')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue
                    
                    try:
                        if direcao == 1:
                            if (tab_montado[i][j-2], tab_montado[i][j-1], tab_montado[i][j], tab_montado[i][j+1], tab_montado[i][j+2]) == (0,0,0,0,0):

                                tab_montado[i][j-2] = 1
                                tab_montado[i][j-1] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i][j+1] = 1
                                tab_montado[i][j+2] = 1
                                p5 -= 1
                        
                        elif direcao == 2:
                            if (tab_montado[i-2][j], tab_montado[i-1][j], tab_montado[i][j], tab_montado[i+1][j], tab_montado[i+2][j]) == (0,0,0,0,0):

                                tab_montado[i-2][j] = 1
                                tab_montado[i-1][j] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i+1][j] = 1
                                tab_montado[i+2][j] = 1
                                p5 -= 1

                        else:
                            print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                            input('Pressione qualquer tecla para inserir novas entradas... ')
                            continue

                    except:
                        print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue

        print('antefinal')
        # Aqui o tabuleiro montado pelo jogador é adicionado à lista                     
        tabs_montados.append(tab_montado.copy())
        tab_montado = gerar_tabuleiro() # Resetando o tabuleiro para o próximo jogador montar

        print('final')
        #os.system('cls') # Limpando o terminal para o próximo jogador

    return tabs_montados


# Função usada para salvar um jogo no meio, usando os devidos parâmetros necessários
def salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):
    save_usuario = fr'{str(caminho)}\{nome}.py'
    save = open(save_usuario, 'w')
    save.write(f'tab1 = {tab1}\n'
               f'tab2 = {tab2}\n'
               f'tab_de_jogo1 = {tab_de_jogo1}\n'
               f'tab_de_jogo2 = {tab_de_jogo2}\n'
               f'turno = {turno}')
    save.close()


def ataque(jogador, tab, tab_de_jogo, turno):

    turno_ = turno

    print('')
    print('=' * 50)
    print(f'                    Jogador {jogador}\n')
    print('=' * 50)
    continuar = int(input('[1] ATACAR\n[2] SALVAR JOGO E SAIR\n> '))
    print('=' * 50)

    if continuar == 2:
        raise ValueError

    elif continuar == 1:

        while turno_ == turno:

            os.system('cls')

            exibir_tab(montar_tab_chute(tab_de_jogo)) # Mostra o tabuleiro de chute

            # Entrada das coordenadas e validação das mesmas
            while True:

                print('')
                ij = input('Insira as coordenadas para o ataque:\n> ').upper()
                print('')


                if ij[0].isdigit():
                    ij = f'{ij[1]}{ij[0]}'


                if not(0 <= int(ij[1]) <= 9) or not('A' <= ij[0] <= 'J'):
                        print('Entrada Inválida!')
                        continue
                else:
                    break

            # Coordenadas de entrada
            j = ord(ij[0].lower()) - 65
            i = int(ij[1])

            # Condicionais para a verificação de acerto
            if tab[i][j] == 0:
                tab_de_jogo[i][j] = 0
                exibir_tab(montar_tab_chute(tab_de_jogo))
                print('=' * 50)
                input('Errou! ')
                turno_ += 1

            elif tab[i][j] == 1:
                tab_de_jogo[i][j] = 1
                exibir_tab(montar_tab_chute(tab_de_jogo))
                print('=' * 50)
                input('Na mosca! Você acertou uma parte do navio inimigo! ')
                tab[i][j] = -1

            elif tab[i][j] == 2:
                tab_de_jogo[i][j] = 2
                exibir_tab(montar_tab_chute(tab_de_jogo))
                print('=' * 50)
                input('Em cheio! Você acertou bem no meio do navio inimigo! ')
                tab[i][j] = -1

            elif tab[i][j] == -1:
                print('=' * 50)
                input('Você já atingiu essa parte do navio! ')


        turno = turno_
        return tab, tab_de_jogo, turno


def fase2(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno=1):

    os.system('cls') # Limpando o terminal para prosseguir para fase 2

    # A ideia do turno é que os turnos impares são do jogador 1, enquanto os turnos pares são do jogador 2
    # Se o jogador acertar o barco, o turno não se altera pois ele joga novamente

    while True:

        if turno % 2 == 1:

            try:
                (tab1, tab_de_jogo2, turno) = ataque(1, tab1, tab_de_jogo2, turno)
                # gera erro se o usuario escolher a opção de salvamento na função ataque()

            except:
                salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                break 


        elif turno % 2 == 0:

            try:
                (tab2, tab_de_jogo1, turno) = ataque(2, tab2, tab_de_jogo1, turno)

            except:
                salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                break 


        #---------------------------------------------------------------------------------------------------------------------
        # Essa parte é bem interessante:
        #   Basicamente, a cada turno, eu verifico se ainda há alguma parte de barco não destruida em ambos os tabuleiros.

        #   Para isso, o primeiro for seleciona cada linha horizontal do tabuleiro, enquanto o segundo verifica cada casa
        # dessa linha. As condicionais verificam se o valor dessa casa é 1 ou 2 (valores que indicam um pedaço de barco não destruido).
        # Se o valor de qualquer casa for 1 ou 2, o valor do parâmetro muda de 0 para 1, indicando que ainda há pedaços de barcos inteiros.

        
        parametro1 = 0
        parametro2 = 0

        for i in range(10):
            for j in range(10):
                if tab1[i][j] == 1 or tab1[i][j] == 2:
                    parametro1 = 1

                if tab2[i][j] == 1 or tab2[i][j] == 2:
                    parametro2 = 1

        # Indica que o Jogador 2 venceu
        if parametro1 != 1:
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

        # Indica que o Jogador 1 venceu
        if parametro2 != 1:
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


# Essa função é utilizada para criar um novo jogo, no modo JxJ
def JvsJ(nome):
    player_tab = fase1()
    tab1 = player_tab[0].copy()
    tab2 = player_tab[1].copy()
    fase2(nome, tab1, tab2, copy.deepcopy(tab_0), copy.deepcopy(tab_0), 1)
    menu_login(nome)

# Importa os elementos necessários para a continuação do jogo salvo do arquivo .py correspondente de cada jogador.
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
        input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
        os.system('cls')
        return -1

#_____________________________________________________________________________________________________________

# MENU PRINCIPAL E DE LOGIN


from rich.console import Console
from rich.markdown import Markdown

# Arquivo com instruções de jogo
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()


# Menu depois de feito o login
def menu_login(nome):

    os.system('cls')  # Limpa o terminal a cada vez que o menu é acessado

    while True:

        # Cabeçalho do menu
        print('')
        print('=' * 30)
        print(f'     Seja Bem-Vindo, {nome}!\n')
        print('=' * 30)
        print('1 - Novo Jogo\n2 - Carregar Jogo\n3 - Logout')
        print('=' * 30)
        escolha = int(input('> '))

        match escolha:

            case 1:  # Novo Jogo

                os.system('cls') 

                # Cabeçalho para a seleção do modo de jogo
                print('')
                print('=' * 30)
                print(f'  Selecione o Modo de Jogo!\n')
                print('=' * 30)
                print('1 - Jogador vs. Máquina\n2 - Jogador vs. Jogador\n3 - Voltar')
                print('=' * 30)
                escolha_ = int(input('> '))

                match escolha_:

                    case 1:
                        ... # A ser adicionado
                    case 2:
                        JvsJ(nome) # Função para criar um novo jogo
                    case 3:
                        continue

            case 2:  # Carregar Jogo
                carregar_jogo(nome)

            case 3:  # Voltar ao menu principal
                main_menu()
                break



# Menu principal de entrada
def main_menu():

    while True:

        os.system('cls') # Limpa o terminal a cada vez que o menu é acessado

        # Cabeçalho do menu
        print('=' * 30)
        print('     💣 Batalha Naval 🛳️')
        print('=' * 30)
        print('1 - Fazer Login\n2 - Cadastrar Usuário\n3 - Como Jogar?\n4 - Sair')
        print('=' * 30)
        escolha = int(input('> '))

        # Seleção de opções
        match escolha:

            case 1:  # Fazer Login

                nome = input('\nInsira o nome de usuário: ')
                senha = input('Digite sua senha: ')

                if login(nome,senha):
                    menu_login(nome)
                else:
                    continue

            case 2:  # Fazer Cadastro
                nome = input('\nInsira o nome de usuário: ')
                senha = input('Escolha uma senha: ')
                cadastros = open('usuarios.txt', 'r')
                if nome in cadastros.read():
                    print('\nJá existe um usuário com esse nome, por favor tente outro!\n')
                else:
                    cadastro(nome,senha)
                cadastros.close()
                continue

            case 3:  # Mostrar instruções de jogo
                os.system('cls')
                Console().print(Markdown(readme))
                input('\n\nPressione qualquer tecla para voltar ao MENU...\n')
                os.system('cls')
            case 4:
                break
    
    exit()




def mach_fase1():

    mach_tab = main_tab.copy()

    d2 = 4  
    c3 = 3  
    e4 = 2 
    p5 = 1  

    while d2 + c3 + e4 + p5 != 0:

        
        barco = random.randint(2,5)
        direcao = random.randint(1,2) # 1 = H e 2 = V

        match barco:
            case 2:
                if direcao == 1:
                    i = random.randint(0,9)
                    j = random.randint(0,8)
                elif direcao == 2:
                    i = random.randint(0,8)
                    j = random.randint(0,9)                    
            case 3:
                if direcao == 1:
                    i = random.randint(0,9)
                    j = random.randint(1,8)
                elif direcao == 2:
                    i = random.randint(1,8)
                    j = random.randint(0,9)
            case 4:
                if direcao == 1:
                    i = random.randint(0,9)
                    j = random.randint(1,7)
                elif direcao == 2:
                    i = random.randint(1,7)
                    j = random.randint(0,9)
            case 5:
                if direcao == 1:
                    i = random.randint(0,9)
                    j = random.randint(2,7)
                elif direcao == 2:
                    i = random.randint(2,7)
                    j = random.randint(0,9)


        #print(barco, direcao, i, j)
        match barco:
            case 2:
                if d2 == 0:
                    continue

                if direcao == 1:
                    if (mach_tab[i][j], mach_tab[i][j+1]) == (0,0):

                        mach_tab[i][j+1] = 1
                        mach_tab[i][j] = 2
                        d2 -= 1
                
                elif direcao == 2:
                    if (mach_tab[i][j], mach_tab[i+1][j]) == (0,0):

                        mach_tab[i+1][j] = 1
                        mach_tab[i][j] = 2
                        d2 -= 1

            case 3:
                if c3 == 0:
                    continue
                
                if direcao == 1:
                    if (mach_tab[i][j-1], mach_tab[i][j], mach_tab[i][j+1]) == (0,0,0):


                        mach_tab[i][j-1] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i][j+1] = 1
                        c3 -= 1
                
                elif direcao == 2:
                    if (mach_tab[i-1][j], mach_tab[i][j], mach_tab[i+1][j]) == (0,0,0):

                        mach_tab[i-1][j] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i+1][j] = 1
                        c3 -= 1


            case 4:
                if e4 == 0:
                    continue

                if direcao == 1:
                    if (mach_tab[i][j-1], mach_tab[i][j], mach_tab[i][j+1], mach_tab[i][j+2]) == (0,0,0,0):


                        mach_tab[i][j-1] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i][j+1] = 1
                        mach_tab[i][j+2] = 1
                        e4 -= 1
                
                elif direcao == 2:
                    if (mach_tab[i-1][j], mach_tab[i][j], mach_tab[i+1][j], mach_tab[i+2][j]) == (0,0,0,0):

                        mach_tab[i-1][j] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i+1][j] = 1
                        mach_tab[i+2][j]
                        e4 -= 1


            case 5:
                if p5 == 0:
                    continue
                
                if direcao == 1:
                    if (mach_tab[i][j-2], mach_tab[i][j-1], mach_tab[i][j], mach_tab[i][j+1], mach_tab[i][j+2]) == (0,0,0,0,0):

                        mach_tab[i][j-2] = 1
                        mach_tab[i][j-1] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i][j+1] = 1
                        mach_tab[i][j+2] = 1
                        p5 -= 1
                
                elif direcao == 2:
                    if (mach_tab[i-2][j], mach_tab[i-1][j], mach_tab[i][j], mach_tab[i+1][j], mach_tab[i+2][j]) == (0,0,0,0):

                        mach_tab[i-2][j] = 1
                        mach_tab[i-1][j] = 1
                        mach_tab[i][j] = 2
                        mach_tab[i+1][j] = 1
                        mach_tab[i+2][j]
                        p5 -= 1
                    
                
    return mach_tab

def mach_fase2():
    ...


main_menu()
