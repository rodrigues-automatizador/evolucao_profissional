from multiprocessing import Process, Queue

def worker(q):
    q.put("Olá mundo!")
    
if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    
    p.start()
    p.join()
    
    message = q.get()
    print(message)