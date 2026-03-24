# crie um programa que mostre todos os números pares de 1 a 100

for i in range(2, 101, 2):
    print(i)
    
numero = 2
while numero <= 100:
    print(numero)
    numero += 2
    
numero = 1
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)