# Crie um programa que verifique se um número digitado
# pelo usuário é perfeito.

numero = int(input("Digite um número para descobrir se o mesmo é perfeito: "))
numero_perfeito = []

for i in range(1, numero):
    if numero % i == 0:
        numero_perfeito.append(i)

if sum(numero_perfeito) == numero:
    print(f"O número {numero} é perfeito: {numero_perfeito}")

else:
    print(f"O número {numero} não é perfeito!")
    
        