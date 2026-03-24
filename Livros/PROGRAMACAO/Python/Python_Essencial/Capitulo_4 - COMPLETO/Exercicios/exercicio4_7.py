# Crie um programa que peça ao usuário para digitar um nome de usuário
# e uma senha contendo apenas caracteres alfanuméricos e use uma
# expressão regular para fazer uma limpeza nos valores digitados,
# exibindo novamente oara o usuário os valores processados.

import re

usuario = input("Digite o nome do usuário: ")
senha = input("Digite uma senha: ")
print("Antes=================")
print(usuario)
print(senha)

print("Depois=================")
resultado = re.sub(r'[^a-zA-Z0-9]', '', usuario)
print(resultado)

resultado = re.sub(r'[^a-zA-Z0-9]', '', senha)
print(resultado)