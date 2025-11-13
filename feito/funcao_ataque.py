import os
from teste0 import tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno

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

def exibir_tab(tab):
    print('  A', '  B', ' C', ' D', ' E', '  F', ' G', ' H', ' I', ' J')
    for linhas in range(10):
        print(linhas, tab[linhas])








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
            j = ord(ij[0].lower()) - 97
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


        turno = turno_
        return tab, tab_de_jogo, turno
    

