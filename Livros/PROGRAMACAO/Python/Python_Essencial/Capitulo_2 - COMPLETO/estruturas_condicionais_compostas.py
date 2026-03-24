# Verificação de maioridade
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")
    
    
# Verificação de aprovação por nota
nota = float(input("Digite sua nota: "))

if nota >= 9:
    print("Você foi aprovado com louvor.")
elif nota >= 7:
    print("Você foi aprovado.")
else:
    print("Você foi reprovado.")
