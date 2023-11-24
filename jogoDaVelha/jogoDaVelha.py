## -----------------------------------------------------
#    Projeto: Jogo da Velha
#    Disciplina: Lógica de Programação
#    Participantes: Hemerson Jhonatan, Alessandra Teixera, Mariana Martins e Leonardo Nascimento
## -----------------------------------------------------
## ----- Funções do usuário
def criaMatriz():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return mat

def apresentaMatriz(mat):
    print(mat[0][0], "|", mat[0][1], "|", mat[0][2])
    print("-" * 10)
    print(mat[1][0], "|", mat[1][1], "|", mat[1][2])
    print("-" * 10)
    print(mat[2][0], "|", mat[2][1], "|", mat[2][2])

def posicaoOcupada(matriz, posicao):
    
    for linha in matriz:
        if linha==0:
            return False
    else: True    
    return 

def registraJogada(mat, posicao, jogador):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == posicao:
                mat[i][j] = jogador
                return mat
    return mat

def trocaJogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"

def verificaGanhador(mat, jogador):
    
    for i in range(3):
        if mat[i][0] == mat[i][1] == mat[i][2] == jogador:
            return True
        if mat[0][i] == mat[1][i] == mat[2][i] == jogador:
            return True
    if mat[0][0] == mat[1][1] == mat[2][2] == jogador:
        return True
    if mat[0][2] == mat[1][1] == mat[2][0] == jogador:
        return True
    return False

print("*** JOGO DA VELHA *** \n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras: ")
print("  a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print("  b) Os números de 1 a 9 representam os espaços que estão livres.")
print("     Você só pode escolher as posições livres.")
print("  c) O vencedor será o primeiro Jogador a preencher uma linha, uma coluna ou uma diagonal.")
print()

matriz = criaMatriz()
jogador = "X"
c = 0
while c < 9:
    apresentaMatriz(matriz)
    posicao = int(input(f"(Jogador {jogador}) Informe a posição desejada: "))
    
    if posicaoOcupada(matriz, posicao):
        print("\nVocê não pode escolher uma posição que já está ocupada. Tente novamente")
    else:
        matriz = registraJogada(matriz, posicao, jogador)
        c += 1
        if verificaGanhador(matriz, jogador):
            apresentaMatriz(matriz)
            print(f"Parabéns! Jogador {jogador} venceu!")
            break
        if c == 9:
            apresentaMatriz(matriz)
            print("Deu velha!")
            break
        jogador = trocaJogador(jogador)
        