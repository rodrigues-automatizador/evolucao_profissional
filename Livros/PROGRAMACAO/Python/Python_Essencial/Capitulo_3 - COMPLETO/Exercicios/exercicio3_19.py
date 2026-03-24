# Crie um programa que verifique se uma palavra é um palindromo

palavra = input("Digite uma palavra: ")

palindromo = palavra[::-1]

if palavra.upper() == palindromo.upper():
    print(f"A palavra: {palavra} é um palíndromo!")

else:
    print(f"A palavra: {palavra} não é um palíndromo!")
