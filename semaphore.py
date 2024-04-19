import threading

# Create a semaphore with initial value 1
s = threading.Semaphore(1)
    t1 = threading.Thread(target=thread_function, args=("Thread 1",))
    t2 = threading.Thread(target=thread_function, args=("Thread 2",))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

def P():
    # Wait operation (acquire the semaphore)
    s.acquire()

def V():
    # Signal operation (release the semaphore)
    s.release()

def thread_function(name):
    print(f"{name} attempting to acquire semaphore")
    P()
    print(f"{name} has acquired semaphore")
    # Simulate some operation
    threading.Event().wait(2)  # Represents the task being done while holding the semaphore
    print(f"{name} releasing semaphore")
    V()




