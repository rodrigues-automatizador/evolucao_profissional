# Crie um programa que leia o nome, o salário e o valor do imposto de uma pessoa,
# como entrada e imprima, ao fim, uma saída no seguinte formato: 
# "Fulano tem um salário líquido de R$ 1.800,00"

nome = input("Digite o nome do Funcionário: ")
salario = float(input("Digite o salário do Funcionário: "))
imposto = float(input("Digite o valor do imposto: "))

print(f"Nome: {nome}")
print(f"Salário: {salario}")

salario *= (1 - (imposto / 100)) 

print(f"O Funcionário {nome} tem um salário líquido de R$ {salario:.2f}")