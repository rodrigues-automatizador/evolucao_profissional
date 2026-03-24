import os
import shutil

# Exemplo 1 criando e excluindo diretórios

os.mkdir('meudiretorio')
os.rmdir('meudiretorio')


# Exemplo 2 renomeando e excluindo arquivos

os.rename('meu-arquivo.txt', 'meuarquivo_novo.txt')
os.remove('meuarquivo_novo.txt')

# Exemplo 3
shutil.copy('meu-arquivo.txt', 'diretorio_novo/meuarquivo.txt')