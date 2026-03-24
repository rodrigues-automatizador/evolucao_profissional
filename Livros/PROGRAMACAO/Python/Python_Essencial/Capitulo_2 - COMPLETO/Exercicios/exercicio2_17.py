# Crie um programa que pergunte ao usuário sua idade e exiba uma mensagem de acordo
# com as seguintes regras: você é jovem se a idade for menor do que 21 anos,
# você é adulto se sua idade for entre 21 e 60 anos;
# Você é idoso caso a idade seja superior a 60 anos

idade = int(input("Digite sua idade: "))

if idade < 21 and idade >= 0:
    print("Você é menor de idade")
    
elif idade >= 21 and idade <= 60:
    print("Você é maior de idade!")

elif idade > 60:
    print("Você é idoso!")
    
else:
    print("Idade inválida!")