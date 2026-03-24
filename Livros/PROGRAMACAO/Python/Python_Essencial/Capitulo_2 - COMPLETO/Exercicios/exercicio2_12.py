# Crie um programa que verifique se uma pessoa é elegível para aposentadoria
# ( Se tem mais de 60 anos ou mais para mulheres e 65 anos ou mais para homens)

idade = int(input("Digite a idade do trabalhador: "))
genero = input("Digite o gênero do trabalhador: ")

genero = genero.upper()

if genero == "MASCULINO" and idade >= 65:
    print("Trabalhador elegível para aposentadoria!")
    
elif genero == "FEMININO" and idade >= 60:
    print("Trabalhadora elegível para aposentadoria!")
    
else:
    print("Trabalhador não elegível!")
    