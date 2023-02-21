# Exercicio 9
# Elabore um programa python que permita, através da inserção dos lados de um
# triângulo, identificar de que tipo de triângulo se trata (isósceles – dois lados iguais e
# um diferente, equilátero – todos os lados iguais, escaleno – se todos os lados forem
# diferentes).

lados_triangulo = []

for i in range(3):
    numero = float(input("Introduza o lado do triangulo:"))
    lados_triangulo.append(numero)


if lados_triangulo[0] == lados_triangulo[1] == lados_triangulo[2]:
    print("Equilatero")
elif lados_triangulo[0] == lados_triangulo[1] or lados_triangulo[1] == lados_triangulo[2] or lados_triangulo[2] == \
        lados_triangulo[0]:
    print("Isosceles")
else:
    print("Escaleno")
