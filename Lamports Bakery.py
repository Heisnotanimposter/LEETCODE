import threading
import time

THREAD_COUNT = 8

tickets = [0] * THREAD_COUNT
choosing = [0] * THREAD_COUNT
resource = 0
resource_lock = threading.Lock()

def lock(thread):
    global tickets, choosing

    choosing[thread] = 1
    max_ticket = max(tickets)
    tickets[thread] = max_ticket + 1

    choosing[thread] = 0

    for other in range(THREAD_COUNT):
        while choosing[other]:
            time.sleep(0)  # Yield control to other threads

        while tickets[other] != 0 and (tickets[other] < tickets[thread] or
                                       (tickets[other] == tickets[thread] and other < thread)):
            time.sleep(0)  # Yield control to other threads

def unlock(thread):
    global tickets
    tickets[thread] = 0

def use_resource(thread):
    global resource
    with resource_lock:
        if resource != 0:
            print(f"Resource was acquired by {thread}, but is still in-use by {resource}!")
        resource = thread
        print(f"{thread} using resource...")
        time.sleep(2)  # Simulate resource usage
        resource = 0

def thread_body(thread):
    lock(thread)
    use_resource(thread)
    unlock(thread)

    threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=thread_body, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
