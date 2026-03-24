# Verificação de estrutura condicional aninhada
a, b, c = 10, 20, 30

if a > b:
    if a > c:
        print("A é o maior número.")
    else:
        print("C é o maior número.")
        
else:
    if b > c:
        print("B é o maior número.")
    else:
        print("C é o maior número.")