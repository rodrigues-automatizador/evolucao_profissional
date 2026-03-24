# Faça um programa que use dict compreehension para criar um dicionário 
# com as raízes quadradas dos números de 1 a 10. Utilize os números como 
# chave e as raízes quadradas como valor.

raizes_quadradas = {n: n ** 0.5 for n in range(1, 11)}

print(raizes_quadradas)
