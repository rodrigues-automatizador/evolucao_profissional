# criando um dicionário com pares chave valor
pessoa = {'nome':'João',
          'idade': 30,
          'cidade':'São Paulo'}

# acessando um valor pela sua chave
print(pessoa['nome'])

# alterando o valor associado a uma chave
pessoa['idade'] = 31
print(pessoa['idade'])

# adicionando um novo par chave:valor
pessoa['pais'] = 'Brasil'

print(pessoa)

# removendo um par chave:valor
del pessoa['cidade']
print(pessoa)