import os, pathlib
from funcao_ataque import ataque
from teste0 import tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno

caminho = pathlib.Path('saves').absolute

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

def salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):
    save_usuario = fr'{str(caminho)}\{nome}.py'
    save = open(save_usuario, 'w')
    save.write(f'tab1 = {tab1}\n'
               f'tab2 = {tab2}\n'
               f'tab_de_jogo1 = {tab_de_jogo1}\n'
               f'tab_de_jogo2 = {tab_de_jogo2}\n'
               f'turno = {turno}')
    save.close()








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


fase2('joelson', tab1, tab2, tab_de_jogo1, tab_de_jogo2)