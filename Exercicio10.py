# Exericio10
# Considere uma equação do segundo grau 𝑓(𝑥) = 𝑎 · 𝑥2 + 𝑏 · 𝑥 + 𝑐. A partir dos coeficientes,
# determine as raízes da equação. Dica: ∆ = 𝑏2 - 4 · 𝑎 · 𝑐: se delta é maior que 0, possui duas
# raízes reais; se delta é 0, possui uma raiz; caso delta seja menor que 0, não possui raízes reais.
import math

coef1 = float(input("Introduza o coeficiente do x^2:"))
coef2 = float(input("Introduza o coeficiente do x:"))
coef3 = float(input("Introduza o coeficiente isolado:"))

delta = (2*coef2) - (4 * coef1 * coef3)
print(delta)
if delta > 0:
    raiz1 = ((-coef2) + math.sqrt(delta)) / (2*coef1)
    raiz2 = ((-coef2) - math.sqrt(delta)) / (2 * coef1)

    print("Raiz1:",raiz1)
    print("Raiz2:",raiz2)

elif delta == 0:
    raiz = (-coef2) / (2*coef1)
    print("Raiz:", raiz)

else:
    print("Não tem razies reais")
