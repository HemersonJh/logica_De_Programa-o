a = 0
soma = 0
while a<10:
    a+=1
    preco = float(input("Preço do produto " +str(a)+ ": "))
    soma+=preco
print(f"valor total= R$ {soma:.2f}")