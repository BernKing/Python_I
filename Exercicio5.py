#Exericio5


#Elabore um programa python que faça a classificação qualitativa de uma nota de um aluno
#segundo os seguintes níveis: [0,5[ = péssimo; [5,8[ = mau; [8,10[ = insuficiente;
#[10,12[ = suficiente; [12,16[ = bom; [16,20] = excelente. Valide o valor introduzido.

while True:
    nota = int(input("Nota: "))

    if 0 <= nota < 5:
        print("Pessimo")
        break
    elif 5 <= nota < 8:
        print("Mau")
        break
    elif 8 <= nota < 10:
        print("Insuficiente")
        break
    elif 10 <= nota < 12:
        print("Suficiente")
        break
    elif 12 <= nota < 16:
        print("Bom")
        break
    elif 16 <= nota < 20:
        print("Excelente")
        break
