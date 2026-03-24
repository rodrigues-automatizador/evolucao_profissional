# crie um programa que verifique se um texto digitado
# é um palindromo ou não

palavra = input("Digite uma palavra: ")
palindromo = palavra[::-1]

if palavra == palindromo:
    print(f"A palavra digitada {palindromo} é um palíndromo")
    
else:
    print(f"A palavra digitada {palindromo} não é um palíndromo")