c=0
votosA=0
votosB=0
voto = int
while c<10:
    c=c+1
    int(input("Digite o voto 1 ou 2: " ))
    if voto == 1:
        votosA = votosA+1
    else:
        votosB=votosB+1
print("Votos de candidato A", votosA)
print("Votos de candidato B", votosB)

