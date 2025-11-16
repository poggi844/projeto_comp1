import random as r
import os
from main import montar_main_tab, salvar_jogo, ataque
from teste0 import tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno

def posicoes():
    tab = []
    for i in range(10):
        for j in range(10):
            tab.append((i,j))
    return tab
lista_posicoes = posicoes()


def ataque_mach(tab, turno, clean_list, coord_ataque=(-1,-1)):

    turno_ = turno

    while turno_ == turno:

            
        if coord_ataque == (-1,-1):
            index = clean_list.index(r.choice(clean_list))
            (i,j) = clean_list[index]

        else:
            index = clean_list.index(coord_ataque)
            (i,j) = coord_ataque


        if tab[i][j] == 0:
            tab[i][j] = 3
            clean_list.pop(index)

            montar_main_tab(tab)
            input('\nO inimigo errou!  ')

            turno_ += 1


        elif tab[i][j] == 1:
            tab[i][j] = -1
            clean_list.pop(index)

            montar_main_tab(tab)
            input('\nO inimigo atingiu um de seus barcos!  ')
        
            direcao = 1
            sentido = r.choice([-1,1])

            if direcao == 1:
                if (i, j+sentido) in clean_list:
                    ataque_mach(tab, turno, clean_list, (i,j+sentido))

            elif direcao == 2:
                if (i+sentido, j) in clean_list:
                    ataque_mach(tab, turno, clean_list, (i+sentido, j))


        elif tab[i][j] == 2:
            tab[i][j] = -1
            clean_list.pop(index)

            montar_main_tab(tab)
            input('\nO inimigo atingiu um de seus barcos!  ')

            direcao = 1
            sentido = r.choice([-1,1])

            if direcao == 1:
                if (i, j+sentido) in clean_list:
                    ataque_mach(tab, turno, clean_list, (i,j+sentido))

            elif direcao == 2:
                if (i+sentido, j) in clean_list:
                    ataque_mach(tab, turno, clean_list, (i+sentido, j))
                  
        turno = turno_
        return tab, turno, clean_list


def mach_fase2(nome, tab1, tab2, tab_de_jogo2, turno=1):

    os.system('cls')

    clear_list = lista_posicoes


    while True:

        if turno % 2 == 1:

            try:
                (tab2, tab_de_jogo2, turno) = ataque(1, tab2, tab_de_jogo2, turno)


            except:
                salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                break 


        elif turno % 2 == 0:

            (tab1, turno, clear_list) = ataque_mach(tab1, turno, clear_list)
            

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


mach_fase2('teste0', tab1, tab2, tab_de_jogo2)