import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
win = True
jogada = True
coorde = 1
start = 1


while start == 1:
    limpar()
    print("Vamos começar!!\n\n")


    while win:
        limpar()


        for i in range(3):
            print(tabuleiro[i][0],"|",tabuleiro[i][1],"|",tabuleiro[i][2])


        coorde = list(map(int,input("\nQual a coordenada da jogada?(escreva em x,y)\nR: ").split(",")))


        if tabuleiro[coorde[0]-1][coorde[1]-1] == " ":
            if jogada:
                tabuleiro[coorde[0]-1][coorde[1]-1] = "X"
            else:
                tabuleiro[coorde[0]-1][coorde[1]-1] = "O"
        else:
            while tabuleiro[coorde[0]-1][coorde[1]-1] != " ":
                limpar()


                for i in range(3):
                    print(tabuleiro[i][0],"|",tabuleiro[i][1],"|",tabuleiro[i][2])


                coorde = map(-1,list(map(int,input("\nJogada Inválida!!\nQual a coordenada da jogada?(escreva em x,y)\nR: ").split(","))))

            if jogada:
                tabuleiro[coorde[0]-1][coorde[1]-1] = "X"
            else:
                tabuleiro[coorde[0]-1][coorde[1]-1] = "O"

        for i in range(3):
            if tabuleiro[i][0]==tabuleiro[i][1] and tabuleiro[i][1]==tabuleiro[i][2]:
                win = not win



        jogada = not jogada



    print(f"{'O' if win else 'X'} ganhou!!")
    start = int(input("Quer continuar jogando?\n1.Sim\n2.não\nR: "))