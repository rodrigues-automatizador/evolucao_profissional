import threading
import time

def wait_for_event(e):
    print("Esperando pelo evento")
    e.wait()
    print("Detectei o evento!")
    
e = threading.Event()
t1 = threading.Thread(target=wait_for_event, args=(e,))
t1.start()

time.sleep(2)
e.set()