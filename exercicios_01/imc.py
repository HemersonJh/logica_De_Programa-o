sexo = int(input("Sexo 1 (Masculino) ou 2 (Feminino): "))
altura = float(input("Digite sua Altura: "))
idade = int(input("Idade: "))
#Teste sexo masculino
if sexo ==1:
    altura > 1.70 
    idade <= 40
    peso_ideal = (72.7*altura) -58
    if idade >40:
        peso_ideal = (72.7*altura)-45
elif sexo ==1:
    altura <=1.70
    idade <=40
    idade >40
    peso_ideal = (72.7*altura)-50
    if idade > 40:
        peso_ideal=(72.7*altura)-58
#Teste sexo feminino
if sexo ==2:
    altura >1.50
    peso_ideal =(62.1*altura)-45
elif sexo==2:
    altura<= 1.50
    idade >=35
    peso_ideal=(62.1*altura)-49
elif sexo==2:
    idade <35
    peso_ideal=(62.1*altura)-49
print("Peso ideal: ", peso_ideal)
