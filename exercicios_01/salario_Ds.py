horas = int(input("N° de Horas: "))
nivel = int(input("Nivel do Professor: "))
if nivel == 1:
    sal = horas*32.80
if nivel == 2:
    sal = horas * 44.15
if nivel == 3:
    sal = horas * 52.21
print("Salário= ", sal)
