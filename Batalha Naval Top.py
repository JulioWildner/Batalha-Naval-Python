import time   # importa modulos time para time.sleep e random para jogadas do pc
import random #

def carinha_sad(): # se nao jogar novamente carinha sad a cada 3 segundos ;-;
    while True:
        print(' ;-; ')
        time.sleep(3)
        
def All(): # print para um titulo legalzinho...
    print('\n\n')
    print('IIIIIIII      IIII   IIIIIIIIIIII    IIII     II         II     II     IIII      II')
    print('II     II    IIIIII       II        IIIIII    II         II     II    IIIIII     II')
    print('II     II   III  III      II       III  III   II         II     II   III  III    II')
    print('IIIIIIII    II    II      II       II    II   II         IIIIIIIII   II    II    II')
    print('II     II   IIIIIIII      II       IIIIIIII   II         II     II   IIIIIIII    II')
    print('II     II   II    II      II       II    II   II         II     II   II    II    ')
    print('IIIIIIII    II    II      II       II    II   IIIIIIII   II     II   II    II    II')
    print('\n\n---------------------------------------------------------------------------------------->')
          
    table1 = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],# tabuleiro do jogador
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█']]

    table2 = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],# tabuleiro do computador
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█']]

    fake = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'], # tabuleiro sem nenhuma modificação, para ocultar os navios do pc
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'], # as jogadas em table2 marcam X (acerto) ou O (erro) em fake, que exibe na tela para o jogador
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
              ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█']]


    lado = [' 1 =',' 2 =',' 3 =',' 4 =',' 5 =',' 6 =',' 7 =',' 8 =',' 9 =','10 =','11 =','12 =','13 =','14 =','15 =','16 =','17 =','18 =','19 =','20 ='] # print indica as linhas

    xnavios = [1,1,1,1,1]
    ynavios = [1,1,1,1,1]

    def print_tab1(): # printa o tabuleiro do jogador
        cont = 0
        print('     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20  >>>  Tabuleiro do') #print serve para indicar colunas
        print('     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |          Jogador')
        for linha in table1: 
            print(lado[cont],'  '.join(linha))
            cont += 1
        cont = 0
        
    def print_tab2():# printa tabuleiro do computador
        cont = 0
        print('     01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20  >>>  Tabuleiro do')
        print('     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |         Computador')
        for linha in fake:
            print(lado[cont],'  '.join(linha))
            cont += 1
        cont = 0

    def final1(): # mensagem exibe vitória do jogador e pede se quer jogar novamente
        print_tab2()
        print('=================================================')
        print('>>> O JOGADOR GANHOU DO COMPUTADOR!')
        print('>>> OBRIGADO POR JOGAR!')
        print('=================================================')
        while True:
            l = str(input('Jogar Novamente?(s/n): '))
            if l == 's' or l == 'S':
                All()
            if l == 'n' or l == 'N':
                carinha_sad()
            else:
                print('Entrada inválida!')
                time.sleep(1)
    def final2(): # mensagem exibe vitória do computador e pede se quer jogar novamente
        print_tab1()
        print('=================================================')
        print('>>> O COMPUTADOR GANHOU DO JOGADOR!')
        print('>>> OBRIGADO POR JOGAR!')
        print('=================================================')
        while True:
            l = str(input('Jogar Novamente?(s/n): '))
            if l == 's' or l == 'S':
                All()
            if l == 'n' or l == 'N':
                carinha_sad()
            else:
                print('Entrada inválida!')
                time.sleep(1)

    def posiciona_pc(): # aqui será sorteado posiçoes para o pc colocar seus navios no tabuleiro, aleatorio em horizontal e vertical, com posiçoes aleatórias dentro dos limites do tabuleiro e sem colisao de navios
        k = random.randint(1,2)
        a = random.randint(0,15); f = random.randint(0,15)
        b = random.randint(0,16); g = random.randint(0,16)
        c = random.randint(0,17); h = random.randint(0,17)
        d = random.randint(0,17); i = random.randint(0,17)
        e = random.randint(0,18); j = random.randint(0,18)
        if ynavios[0] == 1 and k == 1:
            if table2[a][f] == '█' and table2[a][(f+1)] == '█' and table2[a][(f+2)] == '█' and table2[a][(f+3)] == '█' and table2[a][(f+4)] == '█':
                table2[a][f] = '1'
                table2[a][(f+1)] = '1'
                table2[a][(f+2)] = '1'
                table2[a][(f+3)] = '1'
                table2[a][(f+4)] = '1'
                ynavios[0] = 0
                posiciona_pc()
            else:
                posiciona_pc()
                    
        if ynavios[0] == 1 and k == 2:
            if table2[a][f] == '█' and table2[(a+1)][f] == '█' and table2[(a+2)][f] == '█' and table2[(a+3)][f] == '█' and table2[(a+4)][f] == '█':
                table2[a][f] = '1'
                table2[(a+1)][f] = '1'
                table2[(a+2)][f] = '1'
                table2[(a+3)][f] = '1'
                table2[(a+4)][f] = '1'
                ynavios[0] = 0
                posiciona_pc()
            else:
                posiciona_pc()

        if ynavios[1] == 1 and k == 1:
            if table2[b][g] == '█' and table2[b][(g+1)] == '█' and table2[b][(g+2)] == '█' and table2[b][(g+3)] == '█':
                table2[b][g] = '2'
                table2[b][(g+1)] = '2'
                table2[b][(g+2)] = '2'
                table2[b][(g+3)] = '2'
                ynavios[1] = 0
                posiciona_pc()
            else:
                posiciona_pc()
                
        if ynavios[1] == 1 and k == 2:
            if table2[b][g] == '█' and table2[(b+1)][g] == '█' and table2[(b+2)][g] == '█' and table2[(b+3)][g] == '█':
                table2[b][g] = '2'
                table2[(b+1)][g] = '2'
                table2[(b+2)][g] = '2'
                table2[(b+3)][g] = '2'
                ynavios[1] = 0
                posiciona_pc()
            else:
                posiciona_pc()
                    
        if ynavios[2] == 1 and k == 1:
            if table2[c][h] == '█' and table2[c][(h+1)] == '█' and table2[c][(h+2)] == '█':
                table2[c][h] = '3'
                table2[c][(h+1)] = '3'
                table2[c][(h+2)] = '3'
                ynavios[2] = 0
                posiciona_pc
            else:
                posiciona_pc

        if ynavios[2] == 1 and k == 2:
            if table2[c][h] == '█' and table2[(c+1)][h] == '█' and table2[(c+2)][h] == '█':
                table2[c][h] = '3'
                table2[(c+1)][h] = '3'
                table2[(c+2)][h] = '3'
                ynavios[2] = 0
                posiciona_pc()
            else:
                posiciona_pc()

        if ynavios[3] == 1 and k == 1:
            if table2[d][i] == '█' and table2[d][(i+1)] == '█' and table2[d][(i+2)] == '█':
                table2[d][i] = '4'
                table2[d][(i+1)] = '4'
                table2[d][(i+2)] = '4'
                ynavios[3] = 0
                posiciona_pc()
            else:
                posiciona_pc()
                
        if ynavios[3] == 1 and k == 2:
            if table2[d][i] == '█' and table2[(d+1)][i] == '█' and table2[(d+2)][i] == '█':
                table2[d][i] = '4'
                table2[(d+1)][i] = '4'
                table2[(d+2)][i] = '4'
                ynavios[3] = 0
                posiciona_pc()
            else:
                posiciona_pc()
                    
        if ynavios[4] == 1 and k == 1:
            if table2[e][j] == '█' and table2[e][(j+1)] == '█':
                table2[e][j] = '5'
                table2[e][(j+1)] = '5'
                ynavios[4] = 0
                posiciona_pc()
            else:
                posiciona_pc()

        if ynavios[4] == 1 and k == 2:
            if table2[e][j] == '█' and table2[(e+1)][j] == '█':
                table2[e][j] = '5'
                table2[(e+1)][j] = '5'
                ynavios[4] = 0
                posiciona_pc()
            else:
                posiciona_pc()   

    def pc_ataca(): # Ataque aleatório do computador no tabuleiro do jogador
        while True:
            verifica_navios()
            a = random.randint(0,19); b = random.randint(0,19)
            if table1[a][b] != '█' and table1[a][b] != 'O':
                table1[a][b] = 'X'
                print_tab1()
                print('\nMíssil do Computador Acertou!\n')
                break
            elif table1[a][b] == '█':
                table1[a][b] = 'O'
                print_tab1()
                print('\nMíssil do Computador Errou!\n')
                break
            time.sleep(2)
            atacar()
        
    def atacar(): # ataque em posiçao escolhida pelo jogador no tabuleiro do computador
        while True:
            while True:
                verifica_navios()
                time.sleep(2)
                print_tab2()
                z = str(input('\nAtacar qual coluna? (1-20): '))
                if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                    p = int(z)
                    p -= 1
                    break
                else:
                     print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.\n')
                     time.sleep(1)
                     
            while True:
                z = str(input('Atacar qual linha? (1-20): '))
                if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                    z = int(z)
                    z -= 1
                    break
                else:
                     print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.\n')
                     time.sleep(1)
            
            while True:         
                if table2[z][p] != '█' and table2[z][p] != 'O':
                    fake[z][p] = 'X'
                    print('\nMíssil do Jogador Acertou!\n')
                    break
                elif table2[z][p] == '█':
                    fake[z][p] = 'O'
                    print('\nMíssil do Jogador Errou!\n')
                    break
                elif table2[z][p] == 'O' and table2 == 'X':   
                    print('\nVocê já lançou aí!\n')
            time.sleep(2)
            pc_ataca()
            
    def verifica_navios(): # verifica se alguem ganhou, total de X no tabuleiro dado a soma dos tamanhos no navio é de 17, portanto quem tiver 17 X no tabuleiro perde.
        cont = 0 
        for line in table1:
            for val in line:
                if val == 'X':
                    cont += 1
        cont2 = 0 
        for line2 in table2:
            for val2 in line2:
                if val2 == 'X':
                    cont2 += 1
        if cont == 17:
            final2()
        if cont2 == 17:
            final1()
        
    def jogando(): # printar infomaçoes sobre navios e escolhas
        print('---------------------------------------------------------------------------------------->')
        print('Jogador tem:\n1 - Porta-aviões x%s\n2 - Encouraçado x%s\n3 - Submarino x%s\n4 - Destroyer x%s\n5 - Patrulheiro x%s' %(xnavios[0],xnavios[1],xnavios[2],xnavios[3],xnavios[4]))
        print('\nDireção - Navio de Horizontal digite: 1 ; Navio de Vertical digite : 2')
        print('\nNo tabuleiro: "X" marca acerto de míssil. "O" marca erro de míssil.')
        print('---------------------------------------------------------------------->\n')

        if xnavios == [0,0,0,0,0]: # quando navios do jogador ficarem zerados, o ataque começa
            print('----------------')
            print('|Comçar ataque!|')
            print('----------------\n')
            atacar()
        
        while True: # whiles para escolha de navios e posicoes
            x = str(input('>>> Qual navio deseja posicionar?(1-5): '))
            if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
                x = (int(x))-1
                if xnavios[x] == 1:
                    x += 1
                    x = str(x)
                    break
                else:
                    print('!!! Esse navio ja foi posicionado! Tente outro.')
                    time.sleep(1)
                    jogo()
                    
            else:
                print('!!! Entrada inválida, escolha de 1 a 5, sem espaços ou caracteres especiais.')
                time.sleep(1)
                jogo()
        
        while True: # whiles para escolha de navios e posicoes
            y = str(input('>>> Direção Horizontal ou Vertical?(1-2): '))
            if y == '1' or y == '2':
                break
            else:
                print('!!! Entrada inválida, escolha 1 ou 2, sem espaços ou caracteres especiais.')
                time.sleep(1)
                jogo()
                
        while True: # whiles para escolha de navios e posicoes
            z = str(input('>>> Qual coluna? (1-20): '))
            if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                p = int(z)
                p -= 1
                break
            else:
                 print('!!! Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
                 time.sleep(1)
                 jogo()
                 
        while True: # whiles para escolha de navios e posicoes
            z = str(input('>>> Qual linha? (1-20): '))
            if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                z = int(z)
                z -= 1
                break
            else:
                 print('!!! Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
                 time.sleep(1)
                 jogo()

        # A PARTIR DAQUI ATÉ O FINAL, ELE VAI INSERIR O NAVIO ESCOLHIDO DE ACORDO COM A POSIÇAO INFORMADA. SE O JOGADOR INFORMAR UMA POSIÇAO DE ESPAÇO INSUFICIENTE NO TABULEIRO PARA O NAVIO, ELE IRA PEDIR PARA COLOCA-LO EM OUTRO LOCAL.
        # TAMBEM VERIFICA SE O NAVIO COLIDE OU NAO COM UM JA INSERIDO NO TABULEIRO, CASO COLIDA, PEDE PARA JOGAR NOVAMENTE
        
        if x == '5' and xnavios[4] == 1:
            if y == '1':
                try:
                    if table1[z][p] == '█' and table1[z][(p+1)] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    xnavios[4] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            if y == '2':
                try:
                    if table1[z][p] == '█' and table1[(z+1)][p] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                    
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    xnavios[4] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            
        if x == '4' and xnavios[3] == 1:
            if y == '1':
                try:
                    if table1[z][p] == '█' and table1[z][(p+1)] == '█' and table1[z][(p+2)] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                        
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    xnavios[3] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            if y == '2':
                try:
                    if table1[z][p] == '█' and table1[(z+1)][p] == '█' and table1[(z+2)][p] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                    
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    xnavios[3] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            
        if x == '3' and xnavios[2] == 1:
            if y == '1':
                try:
                    if table1[z][p] == '█' and table1[z][(p+1)] == '█' and table1[z][(p+2)] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                        
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    xnavios[2] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            if y == '2':
                try:
                    if table1[z][p] == '█' and table1[(z+1)][p] == '█' and table1[(z+2)][p] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                                                      
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    xnavios[2] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            xnavios[2] = 0
                    
        if x == '2' and xnavios[1] == 1:
            if y == '1':
                try:
                    if table1[z][p] == '█' and table1[z][(p+1)] == '█' and table1[z][(p+2)] == '█' and table1[z][(p+3)] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                                                      
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    xnavios[1] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            if y == '2':
                try:
                    if table1[z][p] == '█' and table1[(z+1)][p] == '█' and table1[(z+2)][p] == '█' and table1[(z+3)][p] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                                    
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    xnavios[1] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()

        if x == '1' and xnavios[0] == 1:
            if y == '1':
                try:
                    if table1[z][p] == '█' and table1[z][(p+1)] == '█' and table1[z][(p+2)] == '█' and table1[z][(p+3)] == '█' and table1[z][(p+4)] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                                                      
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    p += 1
                    table1[z][p] = x
                    xnavios[0] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
            if y == '2':
                try:
                    if table1[z][p] == '█' and table1[(z+1)][p] == '█' and table1[(z+2)][p] == '█' and table1[(z+3)][p] == '█' and table1[(z+4)][p] == '█':
                        print('Navio do Jogador posicionado!\n')
                        time.sleep(1)
                        
                                                      
                    else:
                        print('\nVocê não pode colocar seu navio. Está colidindo com outro já posicionado! Tente outra vez.')
                        time.sleep(1)
                        jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()
                try:
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    z += 1
                    table1[z][p] = x
                    xnavios[0] = 0
                    jogo()
                except:
                    print('Você não pode colocar seu navio aqui! Ele excede os limites do tabuleiro! Tente outra posição conferindo o tamanho do navio e direção.')
                    time.sleep(1)
                    jogo()

    def jogo(): #DEF JOGO CHAMANDO AS DEFS DE POSICIONAR OS NAVIOS DO PC, PRINTAR O TABULEIRO DO JOGADOR E INICIAR A ENTRADA DOS NAVIOS NO TABULEIRO DO JOGADOR
        posiciona_pc()
        print_tab1()
        jogando()
    
    while True: # VAI INICIAR O JOGO E CONTINUAR A EXECUTA-LO
        jogo()
All()# CHAMA A DEF QUE CONTEM TODO O JOGO PARA INICIAR TUDO
