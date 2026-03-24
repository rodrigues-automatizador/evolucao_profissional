from multiprocessing import Process, Lock

def worker(lock, num):
    with lock:
        print(f"Worker {num} está processando.")
        
if __name__ == '__main__':
    lock = Lock()
    
    for num in range(10):
        Process(target=worker, args=(lock, num)).start()