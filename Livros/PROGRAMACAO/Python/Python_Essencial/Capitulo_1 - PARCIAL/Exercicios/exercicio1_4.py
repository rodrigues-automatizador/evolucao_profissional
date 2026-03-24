# Crie um programa que peça ao usuário para digitar
# seu peso e altura. Em seguida, calcule o índice de massa corporal
# E imprima o resultado

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

resultado = (peso / (altura * altura))
print(f"Seu IMC é: {resultado}")