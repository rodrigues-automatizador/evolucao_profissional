# Crie um programa que calcule e mostre todos os números
# entre 1 e 100 que possuem raíz quadrada exata

lista_raiz_quadrada = [2]

for i in range(2, 10):
    resultado = i * i
    lista_raiz_quadrada.append(resultado)
    
    if resultado == 100:
        break
    
print(lista_raiz_quadrada)

