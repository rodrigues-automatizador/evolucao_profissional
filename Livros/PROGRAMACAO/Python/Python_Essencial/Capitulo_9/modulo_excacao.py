import meu_modulo

def minha_funcao():
    try:
        meu_modulo.funcao_do_modulo()
    except Exception as e:
        print("Erro: " + str(e))