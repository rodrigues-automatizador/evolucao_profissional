import multiprocessing

def worker():
    print("Olá mundo!")
    
if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()    