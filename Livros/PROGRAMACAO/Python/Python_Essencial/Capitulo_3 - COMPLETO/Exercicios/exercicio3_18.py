# Crie um programa que calcule e mostre a sequencia de fibonacci
# até o número digitado pelo usuário

quantidade_fibonacci = int(input("Digite a quantidade de Fibonacci: "))

a, b = 0, 1

for _ in range(1, quantidade_fibonacci):
    resultado = a + b
    a = b
    b = resultado

print(f"A quantidade {quantidade_fibonacci} representa o valor: {b}")