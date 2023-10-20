sexo = input("Digite o sexo: ")
altura = float(input("Digite a altura: "))
idade = int(input("Digite a idade: "))
if sexo =="M":
    if altura >1.70:
        if idade <=40:
            pesoIdeal=(72.7*altura)-58
        else:
            pesoIdeal=(72.7*altura)-45
    else:
        if idade <=40:
            pesoIdeal=(72.7*altura)-50
        else:
            pesoIdeal=(72.7*altura)-58
else:
    if altura >1.50:
        pesoIdeal = (62.1*altura)-44.7
    else:
        if idade >=35:
            pesoIdeal=(62.1 * altura)-45
        else:
            pesoIdeal=(62.1*altura)-49
print("Peso Ideal= ", pesoIdeal)
