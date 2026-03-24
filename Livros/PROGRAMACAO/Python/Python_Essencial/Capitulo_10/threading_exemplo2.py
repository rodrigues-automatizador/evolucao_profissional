import threading 
from time import sleep

contador = 0
lock = threading.Lock()

def worker():
    global contador
    
    with lock:
        contador += 1
        print("Contador: ", contador)
        sleep(0.5)
        
if __name__ == "__main__":
    threads = []
    
    for _ in range(10):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)
        
    for t in threads:
        print("Contador Final: ", contador)