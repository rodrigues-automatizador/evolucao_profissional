# Crie um programa que peça ao usuário para digitar 3 números
# Em seguida, o programa deve calcular e mostrar os valores das raízes
# seguinte equação, usando a fórmular de bhaskara
import math 

# Solicita os coeficientes da equação 
a = float(input("Digite o valor de a: ")) 
b = float(input("Digite o valor de b: ")) 
c = float(input("Digite o valor de c: ")) 

# Calcula o discriminante (delta) 

delta = ((b ** 2) - (4 * a * c))

# Verifica o valor de delta para determinar as raízes 
if delta < 0: 
    print("A equação não possui raízes reais.") 
    
elif delta == 0: 
    raiz = -b / (2 * a)
    print(f"A equação possui uma raiz real: {raiz}") 

else: 
    raiz1 = (-b + math.sqrt(delta)) / (2 * a) 
    raiz2 = (-b - math.sqrt(delta)) / (2 * a) 
    print(f"As raízes da equação são: {raiz1} e {raiz2}")