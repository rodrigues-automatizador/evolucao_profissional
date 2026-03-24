# Crie um programa que calcule e mostre todos os números primos de 1 a 100

def eh_primo(numero):
    
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            return False
    return True

numero_primo = []

for i in range(1, 100):
    if eh_primo(i):
        numero_primo.append(i)
        
print(numero_primo)