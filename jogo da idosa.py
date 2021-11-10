# Jogo da Velha - Henrique P. R. Luz - 1 DT - Prof. Julio Favero - FPOO - Senai 2021 #
# ---------------------------------------------------------------------------------- #

lista_a = [ 0, 1, 2]            # declaração de listas para o game.
lista_b = [ 3, 4, 5]
lista_c = [ 6, 7, 8]

def printar():                  # Função feita para 'encurtar' os "if's" após
    print(lista_a)              # a obtenção da variável "pos".
    print(lista_b)
    print(lista_c)

#def listaa(a):                 # Esta série de funções seria para acessar cada
                                # lista, porém o tamanho do código seria o mesmo.
#def listab(b):
    
#def listac(c):
    

print("***   Jogo da Idosa   ***")      # Início do Jogo

for x in range(0,9):                    # Início do Loop com até 9 'rodadas'.
    print(' ')
    print("Rodada #",x + 1)
    print(' ')
    printar()                           # chamada de Função p/ printar listas.
    print(' ')

    var = str(input("De quem é a vez, [X] ou [O]? ")) #Obtenção de 'var'
    print(' ')
    pos = input("Qual a posição escolhida? ") #Obtenção de 'pos'
    print(' ')
    if pos == '0':                      # Início dos "if's" das listas.
        lista_a[0] = var
        printar()

    if pos == '1':
        lista_a[1] = var
        printar()

    if pos == '2':
        lista_a[2] = var
        printar()

    if pos == '3':
        lista_b[0] = var
        printar()

    if pos == '4':
        lista_b[1] = var
        printar()

    if pos == '5':
        lista_b[2] = var
        printar()

    if pos == '6':
        lista_c[0] = var
        printar()

    if pos == '7':
        lista_c[1] = var
        printar()

    if pos == '8':
        lista_c[2] = var          # fim de série de "if's" relacionadas a cada posição 
        printar()                 # nas linhas.  



        # Início de condições para que o fim do jogo por vitória seja realizado.
    
    if lista_a[0] == lista_b[0] == lista_c[0]:
        print(' ')
        print("XABLAU!")
        break

    if lista_a[1] == lista_b[1] == lista_c[1]:
        print(' ')
        print("XABLAU!")
        break

    if lista_a[2] == lista_b[2] == lista_c[2]:
        print(' ')
        print("XABLAU!")
        break




    if lista_a[0] == lista_a[1] == lista_a[2]:
        print(' ')
        print("XABLAU!")
        break

    if lista_b[0] == lista_b[1] == lista_b[2]:
        print(' ')
        print("XABLAU!")
        break

    if lista_c[0] == lista_c[1] == lista_c[2]:
        print(' ')
        print("XABLAU!")
        break




    if lista_a[0] == lista_b[1] == lista_c[2]:
        print(' ')
        print("XABLAU!")
        break

    if lista_a[2] == lista_b[1] == lista_c[0]:
        print(' ')
        print("XABLAU!")
        break


        # Condição em que SE a vitória não seja atingida antes da Rodada 9,
        # É impresso "DEU VELHA!".

    if x == 8:
        print(' ')
        print("***   DEU RUIM... DEU VELHA!   ***")
        break

    
    #res = input("[s] [n]")   #Este pedaço foi feito no começo do código, para
    #if res == 's':           #pará-lo em certa condição.
    #    break
