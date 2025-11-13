import os
from juncao import main_tab, montar_main_tab, gerar_tabuleiro

def fase1():

    tabs_montados = [] # Local onde irá ser armazenado os tabuleiros feitos pelos jogadores
    tab_montado = main_tab.copy() # Tabuleiro em que o jogador irá montar o seu próprio em cima do tabuleiro base (main_tab)

    for jogador in range(2): # O código se repete para os dois jogadores

        os.system('cls') # Limpando o terminal para começar a fase 1

        # Quantidades de cada tipo de barco.

        d2 = 3  # Destróier
        c3 = 0  # Cruzador
        e4 = 0  # Encouraçado
        p5 = 1  # Porta-aviões

        while d2 + c3 + e4 + p5 != 0: # O turno do jogador roda até acabar os barcos

            os.system('cls') 

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
                            if (tab_montado[i-2][j], tab_montado[i-1][j], tab_montado[i][j], tab_montado[i+1][j], tab_montado[i+2][j]) == (0,0,0,0):

                                tab_montado[i-2][j] = 1
                                tab_montado[i-1][j] = 1
                                tab_montado[i][j] = 2
                                tab_montado[i+1][j] = 1
                                tab_montado[i+2][j]
                                p5 -= 1

                        else:
                            print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                            input('Pressione qualquer tecla para inserir novas entradas... ')
                        
                        continue

                    except:
                        print('\nO NAVIO não cabe na COORDENADA selecionada.\n')
                        input('Pressione qualquer tecla para inserir novas entradas... ')
                        continue


        # Aqui o tabuleiro montado pelo jogador é adicionado à lista                     
        tabs_montados.append(tab_montado.copy())
        tab_montado = gerar_tabuleiro() # Resetando o tabuleiro para o próximo jogador montar

        os.system('cls') # Limpando o terminal para o próximo jogador

    return tabs_montados

fase1()