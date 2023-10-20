cliente = int(input("Tipo de Cliente: "))
valor_Kw = float(input("valor_Kw: "))
if cliente ==1:
    valor_conta = valor_Kw * 0.60
elif cliente ==2:
    valor_conta = valor_Kw * 0.48
elif cliente ==3:
    valor_conta = valor_Kw * 0.15
else:
    print("valor_Kw Invalido")
    valor_conta = 0
print("Valor conta = ", valor_conta)