# Crie um programa que peça ao usuário para inserir 2 números
# complexos e calcule a soma e o produto desses números

numero1 = complex(input("Digite o primeiro número complexo: "))
numero2 = complex(input("Digite o segundo número complexo: "))

soma = numero1 + numero2
produto = numero1 * numero2

print(f"A soma dos números complexos é: {soma}")
print(f"O produto dos números complexos é: {produto}")