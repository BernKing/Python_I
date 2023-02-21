# Exercicio13
# Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o utilizador
# digite um número fora desse intervalo, deverá aparecer uma mensagem informando
# que não existe o mês com este número

#dicionario
meses = [0,"Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

while True:
    mes = int(input("Introduza o numero do mes:"))

    if  1 <= mes <= 12:
        print(meses[mes])
        break

