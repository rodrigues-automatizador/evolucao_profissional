# Crie um generator que produza os números da sequencia de fibonacci. 
# Use este generator para imprimir os primeiros 20 números da sequencia.

def sequencia_fibonacci():
    a, b = 0, 1
    
    while True:
        yield a
        a, b = b, a + b
        
generator = sequencia_fibonacci()
for i in range(100):
    print(next(generator))