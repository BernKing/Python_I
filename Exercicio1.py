#Exercicio1
#Implemente um programa python que peça ao utilizador uma nota de avaliação, valor
#numérico de 0 a 20 (para este exercício não é necessário validar o valor introduzido), e
#que indique se o aluno está APROVADO (>=9.5) ou REPROVADO (<9.5). Atualize o código para
#contemplar, por exemplo: ORAL, para alunos com a nota superior a 16

nota = float(input("Insira a nota:"))

if nota < 9.5:
    print("Reprovado")

elif 9.5 < nota < 16:
    print("Aprovado")

else:
    print("Oral")

