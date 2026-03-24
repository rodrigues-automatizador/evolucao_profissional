import threading
import time

def delayed():
    print("Tarefa executada com atraso proposital.")
    
t1 = threading.Timer(3, delayed)

t1.start()