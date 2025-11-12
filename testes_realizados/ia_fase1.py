import random
from juncao import main_tab , montar_main_tab


def ia_fase1():

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

    

montar_main_tab(ia_fase1())