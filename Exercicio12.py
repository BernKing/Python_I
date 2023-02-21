# Exercicio12
# Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a
# zero e o quadrado do número caso ele seja negativo.
import math

numero1 = float(input("Introduza um numero:"))

if numero1 >= 0:
    print(math.sqrt(numero1))
else:
    print(numero1*numero1)