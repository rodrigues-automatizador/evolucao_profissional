# Exemplo 1

numero = int(input("Digite um número: "))

while numero >= 0:
    print("Você digitou o número", numero)
    numero = int(input("Digite outro número: "))
    
print("Você digitou um número negativo")

# Exemplo 2
numero = 0
while numero <= 10:
    print(numero)
    numero += 2
    
    
# Exemplo 3
soma = 0
contador = 0
numero = float(input("Digite um número: "))

while numero >= 0:
    soma += numero
    contador += 1
    numero = float(input("Digite outro número: "))
    
media = soma / contador
print("A média dos números é", media)

numero = int(input("Digite um número: "))

while True:
    if numero < 0:
        break
    
    print("Você digitou o número", numero )
    
    numero = int(input("Digite outro número: "))

print("Você digitou um número negativo")