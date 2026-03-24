import threading

def worker():
    print("Olá mundo!")
    
if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()
    t.join()