# Crie um programa que peça ao usuário para digitar o valor total de uma venda,
# o percentual de desconto aplicado e imposto. Ao fim o programa deve mostrar o preço final
# da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

valor_venda = float(input("Digite o valor total da venda: "))
desconto = float(input("Digite o percentual do desconto: "))
imposto = float(input("Digite o percentual do imposto: "))

desconto = (1 - (desconto / 100))
valor_venda *= desconto
imposto *= (1 + (imposto / 100))

valor_total = valor_venda + imposto

print(f"O valor da venda com desconto é: {valor_venda}")
print(f"O valor do imposto é: {imposto}")
print(f"O valor total é: {valor_total}")