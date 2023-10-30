maiores=0
idade =1
c = 0
for c in range(1,5,1):
    int(input("Digite sua idade: "))
    if idade >= 18:
        maiores = maiores+1        
print("O total de maiores de idade é", maiores)