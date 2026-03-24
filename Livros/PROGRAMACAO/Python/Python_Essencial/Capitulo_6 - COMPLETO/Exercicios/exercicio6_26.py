# Crie um generator que produza uma sequencia infinita de números inteiros, começando po 1. 
# Em seguida, faça um laço para imprimir os primeiros 10 números dessa sequencia

def sequencia_infinita():
    num = 1
    while True:
        yield num
        num += 1
        
generator = sequencia_infinita()

for i in range(10000):
    print(next(generator))