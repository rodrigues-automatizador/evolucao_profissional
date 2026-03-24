# Crie um programa que peça ao usuário para digitar a base de um triangulo
# Em seguida, o programa deve calcular e mostrar a área desse triângulo.

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = (base * altura) / 2

print(f"A área do triângulo é {area}")