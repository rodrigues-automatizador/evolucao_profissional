# Crie um programa que leia vários números positivos digitados pelo usuário
# até que ele digite um valor negativo. Ao fim, o programa deve mostrar 
# a média dos números positivos

contador, resultado = 0, 0

while True:
    numero = int(input("Digite um número positivo: "))
    
    if numero < 0:
        break

    resultado += numero
    contador += 1
    
resultado /= contador
print(f"A média dos números informados é: {resultado}")