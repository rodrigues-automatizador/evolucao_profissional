# Crie um programa que pergunte ao usuário se peso e sua altura e exiba uma mensagem
# de acordo com seu imc, conforme as seguintes regras: 
# Você está abaixo do peso se for menor que 18,5
# Se estiver entre 18,5 e 24,9 está com peso normal
# acima de 24,9 está acima do peso.
# Por fim você está com obesidade acima dos 29,9

peso = float(input("Digite seu peso corporal: "))
altura = float(input("Digite sua altura em cm: "))

altura /= 100

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Você está abaixo do peso ideal, IMC: {imc}")

elif imc >= 18.5 and imc <= 24.9:
    print(f"Você está com peso normal IMC: {imc}")
    
elif imc >= 25 and imc <= 29.9:
    print(f"Você está com sobrepeso IMC: {imc}")
    
else:
    print(f"Você está com obesidade IMC: {imc}")