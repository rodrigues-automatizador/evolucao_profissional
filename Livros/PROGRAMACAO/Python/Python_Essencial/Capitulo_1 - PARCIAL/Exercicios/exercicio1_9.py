# Crie um programa que peça ao usuário para digitar 2 números quaisquer.
# Em seguida, o programa deve calcular e mostrar a potência do primeiro
# número pelo segundo.

print("Programa calcula Potência")
valor = int(input("Digite o valor para calculo de potência: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = valor ** expoente

print(f"O valor da potencia é: {resultado}")