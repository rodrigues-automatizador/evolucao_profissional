try:
    import meu_modulo 

except ModuleNotFoundError:
    print("Erro: módulo não encontrado!")

try:
    from meu_pacote import minha_funcao 
    
except ImportError:
    print("Erro: função não encontrada!")