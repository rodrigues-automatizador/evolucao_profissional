# Crie um programa que verifique se um número digitado é primo

valor = int(input("Digite um número para verificar se é primo: "))

eh_primo = True

for i in range(2, valor):
    if valor % i == 0:
        eh_primo = False
        print(i)
        break
        
print(f"O número digitado: {valor} é primo? {eh_primo}")
    