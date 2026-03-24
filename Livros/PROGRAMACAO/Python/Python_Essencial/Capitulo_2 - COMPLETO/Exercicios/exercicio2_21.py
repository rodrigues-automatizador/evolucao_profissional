# Crie um programa que simule um semáforo de trânsito. Peça ao usuário para inserir
# a cor atual do semáforo (verde, amarelo ou vermelho) e utilize a estrutura match case
# para imprimir uma ação correspondente. Por exemplo se a cor for verde, imprima prossiga
# se for amarelo imprima prepare-se para parar; se for vermelho, imprima Pare.
# Inclua um caso geral que imprima "cor inválida" para qualquer outra entrada

semaforo = input("Digite uma cor do Semáforo: ")
semaforo = semaforo.upper()

match semaforo:
    case "AMARELO":
        print("Prepare-se para Parar!")
        
    case "VERDE":
        print("Prossiga!")
        
    case "VERMELHO":
        print("Pare!")
        
    case _:
        print("Cor inválida!")