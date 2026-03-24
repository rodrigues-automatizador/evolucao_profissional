import threading
import time

def consumidor(cond):
    with cond:
        print("Consumidor está esperando....")
        cond.wait()
        
        print("Consumidor consumiu o curso.")
        

def produtor(cond):
    with cond:
        print("Produtor está produzindo o recurso...")
        time.sleep(2)
        print("Produtor produziu o recurso.")
        
        cond.notify()
        
        
cond = threading.Condition()
cons = threading.Thread(target=consumidor, args=(cond,))
prod = threading.Thread(target=produtor, args=(cond,))

cons.start()
prod.start()
cons.join()
prod.join()