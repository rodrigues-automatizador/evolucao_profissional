# Exemplo 1
# função lambda que calcula o dobro de um número

dobro = lambda x: x * 2
resultado = dobro(5)
print(resultado)


# Exemplo 2
# função lambda com multiplos parametros

media_ponderada = lambda nota1, peso1, nota2, peso2: (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

resultado = media_ponderada(8, 3, 9, 2)
print(resultado)