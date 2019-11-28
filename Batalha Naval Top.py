import time
import random

table1 = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
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

table2 = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
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

fake = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
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


lado = [' 1 =',' 2 =',' 3 =',' 4 =',' 5 =',' 6 =',' 7 =',' 8 =',' 9 =','10 =','11 =','12 =','13 =','14 =','15 =','16 =','17 =','18 =','19 =','20 =']

xnavios = [1,0,0,0,0]
ynavios = [1,1,1,1,1]

def print_tab1():
    cont = 0
    print('     1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20')
    print('     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |')
    for linha in table1: 
        print(lado[cont],'  '.join(linha))
        cont += 1
    cont = 0
    
def print_tab2():
    cont = 0
    print('     01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20')
    print('     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |')
    for linha in fake:
        print(lado[cont],'  '.join(linha))
        cont += 1
    cont = 0

def posiciona_pc():
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

def pc_ataca():
    while True:
        print_tab1()
        a = random.randint(0,19); b = random.randint(0,19)
        if table1[a][b] != '█' and table1[a][b] != 'O':
            table1[a][b] = 'X'
            print('Míssil do Computador Acertou!')
            u = random.randint(1,4)
            if u == 1:
                while True:
                    a += 1
                    
                
        if table1[a][b] == '█':
            table1[a][b] = 'O'
            print('Míssil do Computador Errou!')
            break
    atacar()
    
def atacar():
    while True:
        print_tab2()
        while True:
            z = str(input('Atacar qual coluna? (1-20): '))
            if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                p = int(z)
                p -= 1
                break
            else:
                 print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
                 time.sleep(1)
                 
        while True:
            z = str(input('Atacar qual linha? (1-20): '))
            if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
                z = int(z)
                z -= 1
                break
            else:
                 print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
                 time.sleep(1)
        
        while True:         
            if table2[z][p] != '█' and table2[z][p] != 'O':
                fake[z][p] = 'X'
                print('Míssil do Jogador Acertou!')
            
            if table2[z][p] == '█':
                fake[z][p] = 'O'
                print('Míssil do Jogador Errou!')
                break
            if table2[z][p] == 'O' and table2 == 'X':   
                print('Você já lançou aí!')
    pc_ataca()
        
    
def jogando():
    
    print('\nJogador tem:\n1 - Porta-aviões x%s\n2 - Encouraçado x%s\n3 - Submarino x%s\n4 - Destroyer x%s\n5 - Patrulheiro x%s' %(xnavios[0],xnavios[1],xnavios[2],xnavios[3],xnavios[4]))
    print('\nDireção - Navio de Horizontal digite: 1 ; Navio de Vertical digite : 2\n')

    if xnavios == [0,0,0,0,0]:
        atacar()
    
    while True:
        x = str(input('Qual navio deseja posicionar?(1-5): '))
        if x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
            x = (int(x))-1
            if xnavios[x] == 1:
                x += 1
                x = str(x)
                break
            else:
                print('Esse navio ja foi posicionado! Tente outro.')
                time.sleep(1)
                jogo()
                
        else:
            print('Entrada inválida, escolha de 1 a 5, sem espaços ou caracteres especiais.')
            time.sleep(1)
            jogo()
    
    while True:
        y = str(input('Direção Horizontal ou Vertical?(1-2): '))
        if y == '1' or y == '2':
            break
        else:
            print('Entrada inválida, escolha 1 ou 2, sem espaços ou caracteres especiais.')
            time.sleep(1)
            jogo()
            
    while True:
        z = str(input('Qual coluna? (1-20): '))
        if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
            p = int(z)
            p -= 1
            break
        else:
             print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
             time.sleep(1)
             jogo()
             
    while True:
        z = str(input('Qual linha? (1-20): '))
        if z == '1' or z == '2' or z == '3' or z == '4' or z == '5' or z == '6' or z == '7' or z == '8' or z == '9' or z == '10' or z == '11' or z == '12' or z == '13' or z == '14' or z == '15' or z == '16' or z == '17' or z == '18' or z == '19' or z == '20':
            z = int(z)
            z -= 1
            break
        else:
             print('Entrada inválida, escolha 1 a 20, sem espaços ou caracteres especiais.')
             time.sleep(1)
             jogo()
    
    if x == '5' and xnavios[4] == 1:
        if y == '1':
            try:
                if table1[z][p] == '█' and table1[z][(p+1)] == '█':
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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
                    print('Navio do Jogador posicionado!')
                    time.sleep(1)
                    print('Navio do Computador posicionando!')
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

def jogo():
    posiciona_pc()
    print_tab1()
    jogando()
    
while True:
    jogo()
