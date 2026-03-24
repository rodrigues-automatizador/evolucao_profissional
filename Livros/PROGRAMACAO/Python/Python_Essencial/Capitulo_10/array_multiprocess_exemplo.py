from multiprocessing import Process, Value, Array

def worker(num, arr):
    num.value = 100
    for i in range(len(arr)):
        arr[i] = -arr[i]
        
if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    
    p = Process(target=worker, args=(num, arr))
    p.start()
    p.join()
    
    print(num.value)
    print(arr[:])