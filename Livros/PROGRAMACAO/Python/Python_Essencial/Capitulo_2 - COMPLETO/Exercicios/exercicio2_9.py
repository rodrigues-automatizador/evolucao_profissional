# Crie um programa que calcule a média de 3 números e exiba a mensagem "Aprovado"
# se a média for maior ou igual a 6 ou "Reprovado" caso contrário. Se a nota for 10
# exiba a mensagem "Parabéns

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = ((nota1 + nota2 + nota3) / 3)

if resultado == 10:
    print("Parabéns você tirou nota máxima!")

elif resultado > 6:
    print("Aprovado!")

else:
    print("Reprovado!")