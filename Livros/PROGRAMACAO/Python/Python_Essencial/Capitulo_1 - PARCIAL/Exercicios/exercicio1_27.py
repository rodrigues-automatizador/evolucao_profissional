# Crie um programa que peça ao usuário para digitar o valor inicial de um investimento,
# a taxa de juros mensal e o número de meses que o valor ficou investido.
# Em seguida, o programa deve calcular e mostrar o valor final considerando,
# o uso de juros compostos.

capital = float(input("Digite o valor de investimento inicial: "))
juros = float(input("Digite a taxa de juros mensal (%): "))
tempo = int(input("Digite a quantidade de meses para o investimento: "))

juros = juros / 100

for _ in range(0, tempo):
    capital *= (1 + juros)
    
print(f"O montante do investimento: {capital:.2f}")