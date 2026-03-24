# Crie um programa que verifique se uma temperatura corporal digitada pelo usuário
# está acima ou abaixo da faixa normal ( 36 a 37º C)

temperatura_corporal = float(input("Digite a temperatura corporal: "))

if temperatura_corporal >= 36 and temperatura_corporal <= 37:
    print("Temperatura corporal normal!")
    
else:
    print("Temperatura anormal!")