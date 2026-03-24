# Crie um programa que peça ao usuário para inserir 2 números
# e calcule a potÊncia do primeiro número pelo segundo número

valor = int(input("Digite um número para a base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = valor ** expoente
print(f"A potência do {valor} é: {resultado}")