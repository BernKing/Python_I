# Exercicio7
# Elabore um programa que de entre dois números fornecidos pelo utilizador, permita
# encontrar o menor deles


numero1 = float(input("Introduza o primeiro numero:"))

numero2 = float(input("Introduza o segundo numero:"))

if numero1 < numero2:
    print(numero1, "<", numero2)
elif numero2 < numero1:
    print(numero2, "<", numero1)
else:
    print(numero1, "=", numero2)


