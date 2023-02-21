# Exercicio8

# Elabore um programa python que de entre três números fornecidos pelo utilizador,
# permita encontrar o maior deles.

numeros = [0, 0, 0]

for i in range(len(numeros)):

    numeros[i] = int(input("Numero:"))


print("O maior dos tres numeros:", max(numeros))