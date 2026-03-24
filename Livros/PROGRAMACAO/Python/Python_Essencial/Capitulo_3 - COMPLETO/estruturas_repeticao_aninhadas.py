# Exemplo 1
for i in range(1,11):
    for j in range(1,11):
        print(i, "x", j, "=", i * j)
    print("==============")
    
# Exemplo 2
numero = 10
e_primo = True

for i in range(2, numero):
    if numero % i == 0:
        e_primo = False
        break
    
if e_primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")