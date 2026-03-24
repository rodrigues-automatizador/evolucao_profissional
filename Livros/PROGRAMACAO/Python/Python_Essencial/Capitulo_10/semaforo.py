import threading
import time

sem = threading.Semaphore(2)

def task():
    sem.acquire()
    print("Tarefa iniciando...")
    
    time.sleep(1)
    print("Tarefa finalizando....")
    sem.release()
    
threads = []
for i in range(10):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()