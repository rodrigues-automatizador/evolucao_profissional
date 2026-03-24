# Crie um programa que verifique se uma letra digitada
# pelo usuário é uma vogal ou consoante

letra = input("Digite uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra digitada é uma vogal")
    
else:
    print("A letra digitada é uma consoante")