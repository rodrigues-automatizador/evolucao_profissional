# importação do módulo math
import math

# seno
angulo = 30
seno = math.sin(math.radians(angulo))
print("Seno de", angulo, "graus:", seno)

#cosseno
cosseno = math.cos(math.radians(angulo))
print("Cosseno de", angulo, "graus:", cosseno)

# arco seno
seno = 0.5
angulo = math.degrees(math.asin(seno))
print("Arco seno de", seno, ":", angulo, "graus")

# arco cosseno
cosseno = 0.5
angulo = math.degrees(math.acos(cosseno))
print("Arco cosseno de", cosseno, ":", angulo, "graus")

# arco tangente
tangente = 1.0
angulo = math.degrees(math.atan(tangente))
print("O arco tangente de", tangente, ":", angulo, "graus")