import datetime
import locale

# Exemplo 1
agora = datetime.datetime.now()
print(agora)


# Exemplo 2
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
agora = datetime.datetime.now()

hora_24 = agora.strftime("%H:%M")
hora_12 = agora.strftime("%I:%M %p")
dia_semana = agora.strftime("%A")
data_formatada = agora.strftime("%d/%m/%Y")

print("Hora em 24 horas: ", hora_24)
print("Hora em 12 horas: ", hora_12)
print(f"São {hora_24} do dia {data_formatada}, que é {dia_semana}.")
print(agora.strftime("%A, %d de %B de %Y, %H:%Mh"))


# Exemplo 3
# Calculando diferenças temporais

data_nascimento = datetime.datetime(1984, 3, 18)
data_atual = datetime.datetime.now()

diferenca = data_atual - data_nascimento
print(f"Você já viveu {diferenca.days} dias.")


# Exemplo 4
# calcular a diferença entre horas.

instante1 = datetime.datetime(2023, 6, 9, 8, 0)
instante2 = datetime.datetime(2023, 6, 9, 18, 30)

diferenca = instante2 - instante1
dif_horas = diferenca.total_seconds() / 3600
print("Diferença em horas: ", dif_horas)

# Exemplo 5
# Adição de tempo

data_original = datetime.datetime(2023, 6, 29)
dez_dias = datetime.timedelta(days=10)
data_nova = data_original + dez_dias

print("Data original: ", data_original)
print("Data nova: ", data_nova)

# Exemplo 6
# Removendo dias 

data_original = datetime.datetime(2023, 6, 29)
cinco_dias = datetime.timedelta(days=5)
data_nova = data_original - cinco_dias

print("Data original: ", data_original)
print("Data nova: ", data_nova)