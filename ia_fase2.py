import random as r
import os
from main import exibir_tab, montar_tab_chute

def ataque_mach(tab, tab_de_jogo, turno, coord = (r.randint(0,9), r.randint(0,9))):

    turno_ = turno

    while turno_ == turno:

        # Entrada das coordenadas e validação das mesmas

        try:
            (i,j) = coord

        
            # Condicionais para a verificação de acerto
            if tab[i][j] == 0:
                tab_de_jogo[i][j] = 0
                turno_ += 1

            elif tab[i][j] == 1:
                tab_de_jogo[i][j] = 1
                tab[i][j] = -1
                
                direcao = r.randint(1,2)

                if direcao == 1:
                    ...
                

            elif tab[i][j] == 2: #meio
                tab_de_jogo[i][j] = 2
                tab[i][j] = -1

                direcao = r.randint(1,2)
                aleatorio = r.choice([-1,1])

                if direcao == 1:
                    
                    if tab[i][j+aleatorio] == -1:
                        if tab[i][j-aleatorio] == -1:
                            ataque_mach(tab, tab_de_jogo, turno)

                    else:
                        ataque_mach(tab, tab_de_jogo, turno, (i, j+aleatorio))

                
                elif direcao == 2:

                    if tab[i+aleatorio][j] == -1:
                        if tab[i-aleatorio][j] == -1:
                            ataque_mach(tab, tab_de_jogo, turno)

                    else:
                        ataque_mach(tab, tab_de_jogo, turno, (i+aleatorio, j))





            
            elif tab[i][j] == -1:
                raise ValueError
            
        except:
            ataque_mach()

                






        turno = turno_
        return tab, tab_de_jogo, turno


def ia_fase2(nome, tab1, tab2, tab_de_jogo1, tab_de_jogo2, turno):

    i = random.randint(0,9)
    j = random.randint(0,9)

    

