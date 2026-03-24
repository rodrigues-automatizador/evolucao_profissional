# Crie um programa que encontre e mostre o maior e o menor número
# em uma lista de 10 números digitada pelo usuário

numeros = []
for _ in range(1, 11):
    valor = int(input("Digite 10 números: "))
    
    numeros.append(valor)

maior_numero = max(numeros)  
menor_numero = min(numeros)

print(f"O maior número encontrado na lista é: {maior_numero}")
print(f"O menor número encontrado na lista é: {menor_numero}")