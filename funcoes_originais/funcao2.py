def fase2(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):

    os.system('cls') # Limpando o terminal para prosseguir para fase 2

    # A ideia do turno é que os turnos impares são do jogador 1, enquanto os turnos pares são do jogador 2
    # Se o jogador acertar o barco, o turno não se altera pois ele joga novamente

    while True:
        if turno % 2 == 1: # Jogador 1

            os.system('cls') # Limpando o terminal

            # Cabeçalho
            print('')
            print('=' * 50)
            print(f'                    Jogador 1\n')
            print('=' * 50)
            continuar = int(input('[1] ATACAR\n[2] SALVAR JOGO E SAIR\n> '))
            print('=' * 50)

            # O jogador tem a opção de atacar (1) uma casa ou salvar o jogo (2)

            match continuar:

                case 1: # ATACAR

                    exibir_tab(montar_tab_chute(tab_de_jogo2)) # Mostra o tabuleiro de chute

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

                case 2: #SALVAR E SAIR

                    salvar_jogo(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno)
                    break 


        # Essa parte do código é equivalente a de cima, porém com o jogador 2

        elif turno % 2 == 0:

            os.system('cls')

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

                    break