#Exericio4

#Implemente um programa em python que converta um valor em bytes para um formato
#humanamente legível (Kilo, Mega, Giga ou Tera bytes consoante o múltiplo que melhor se
#adapte a uma representação de fácil leitura do valor). Considere 1KBytes = 1024 Bytes.
#Exemplo: 16548973 bytes = 15,78 MBytes.
# 1mega = 1024 * 1024 bytes

bytes=float(input("Insira o valor em bytes:"))
if bytes <= 1024:
    print(bytes, " bytes =", bytes, "bytes ")
elif bytes <= 1024 ** 2:
    kilo=bytes/1024
    print(bytes, " bytes =", kilo, " KB ")
elif bytes <= 1024**3:
    mega = bytes / (1024**2)
    print(bytes, " bytes =", mega, "MB ")
elif bytes <= 10244 ** 4:
    giga = bytes / (1024**3)
    print(bytes, " bytes =", giga, "GB ")
else:
    tera = bytes / (1024 ** 4)
    print(bytes, " bytes =", tera, "TB ")



