#Programa Produto
preco_Produto = float(input("Valor Produto: "))
if preco_Produto >= 1.000:
    desconto = 10*preco_Produto/100
    valor_final = preco_Produto - desconto
elif preco_Produto <=1.000:
    desconto = 8*preco_Produto/100
    valor_final = preco_Produto - desconto
print("o Preço é, ", preco_Produto, "desconto: ", desconto," valor final do produto", valor_final)