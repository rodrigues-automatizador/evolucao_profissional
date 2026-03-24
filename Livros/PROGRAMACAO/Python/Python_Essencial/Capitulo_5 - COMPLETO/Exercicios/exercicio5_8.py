# Você é um investigador e precisa decifrar uma mensagem secreta escondida em um texto. 
# Cada letra da mensagem foi substituida em um texto. Cada letra da mensagem foi substituida 
# pela letra do alfabeto que vem imediatamente depois dela. Por exemplo: 
# "a" foi substituida por "b", "b" foi substituida por "c" e assim por diante. 
# A letra "z" foi substituida por "a". Escreva uma função recursiva chamada decifrar_mensagem que 
# aceite a mensagem codificada como uma string e retorne a mensagem decodificada. 
# A regra é que a função deve ser recursiva.

def decifrar_mensagem(mensagem):
    if(len(mensagem)) == 0:
        return mensagem
    else:
        char_decifrado = chr((ord(mensagem[0]) - 98) % 26 + 97)
        return char_decifrado + decifrar_mensagem(mensagem[1:])
    
print(decifrar_mensagem('bdfn'))