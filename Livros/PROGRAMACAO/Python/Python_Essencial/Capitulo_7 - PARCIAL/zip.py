import zipfile

# compactando 3 arquivos em arquivos.zip

with zipfile.ZipFile("arquivo.zip", "w", compresslevel=9, compression=zipfile.ZIP_DEFLATED) as meu_zip:
    meu_zip.write("Capitulo_7 - PARCIAL\arquivo1.txt\arquivo1.txt")
    meu_zip.write("Capitulo_7 - PARCIAL\arquivo1.txt\arquivo2.jpg")
    meu_zip.write("Capitulo_7 - PARCIAL\arquivo1.txt\arquivo3.mp3")
    
    
with zipfile.ZipFile('arquivo.zip', 'r') as meu_zip:
    meu_zip.extractall('/')