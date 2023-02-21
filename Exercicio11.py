# Exercicio11
# Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este
# deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou
# igual a 20, este deverá ser apresentado subtraindo-se 5.

numero1 = int(input("Introduza o primeiro numero: "))
numero2 = int(input("Introduza o segundo numero: "))

soma = numero1 + numero2

if soma > 20:
    print(soma+8)
elif soma <= 20:
    print(soma-5)