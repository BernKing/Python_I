#Exericio2
# Elabore um programa python que permita calcular a média de um aluno atendendo às
# notas obtidas em dois testes. O programa deve apresentar se o aluno foi aprovado ou
# reprovado, tendo em conta que um aluno aprova sempre que a média é superior ou
# igual a 10 valores.

nota1 = float(input("Introduza a nota 1:"))
nota2 = float(input("Introduza a nota 2:"))


media = (nota1 + nota2) / 2
print("Media:", media)
if media < 9.5:
    print("Reprovado")

elif 9.5 < media < 16:
    print("Aprovado")

else:
    print("Oral")