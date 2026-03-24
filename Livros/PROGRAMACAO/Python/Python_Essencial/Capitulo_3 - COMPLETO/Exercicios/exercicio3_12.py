# Crie um programa que calcule e mostre a soma de todos os números primos.

numero_primo = []

def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            return False
        
    return True

for i in range(1, 100):
    if eh_primo(i):
        numero_primo.append(i)
        
print("A soma de todos os números primos é:", sum(numero_primo))