#Exericio3

#Implemente um programa python que converta um par de valores hora, minutos no
#formato 24 horas para o formato AM/PM.
#Exemplo: 13:07  1:07 PM ou 00:07 12:07AM


horas = int(input("Introduza as horas"))
min = int(input("Introduza os minutos"))

if horas == 0:
    print("12",":", min,"AM")
elif  0 < horas < 13:
    print(horas,":",min,"AM")
elif horas >= 13:
    print(horas - 12,":",min,"PM")
