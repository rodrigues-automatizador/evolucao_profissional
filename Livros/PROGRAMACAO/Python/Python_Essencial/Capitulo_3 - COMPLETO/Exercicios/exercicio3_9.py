# Crie um programa que calcule e mostre todos os números 
# divisíveis por 3 ou 5 de 1 a 100.

numero_3 = []
numero_5 = []

for i in range(1, 101):
    if i % 3 == 0:
        numero_3.append(i)
        
    if i % 5 == 0:
        numero_5.append(i)
        
print(f"Números divisíveis por 3 são: {numero_3}")
print(f"Números divisíveis por 5 são: {numero_5}")