import threading

N = 2  # Number of threads (producer and consumer)
flag = [False] * N  # Flags to indicate readiness
turn = 0  # Variable to indicate turn

# Function for producer thread
def producer(j):
    while True:
        flag[j] = True  # Producer j is ready to produce
        turn = 1 - j  # Allow consumer to consume
        while flag[1 - j] and turn == 1 - j:
            # Wait for consumer to finish
            # Producer waits if consumer is ready and it's consumer's turn
            pass

        # Critical Section: Producer produces an item and puts it into the buffer

        flag[j] = False  # Producer is out of the critical section

        # Remainder Section: Additional actions after critical section

# Function for consumer thread
def consumer(i):
    while True:
        flag[i] = True  # Consumer i is ready to consume
        turn = i  # Allow producer to produce
        while flag[1 - i] and turn == i:
            # Wait for producer to finish
            # Consumer waits if producer is ready and it's producer's turn
            pass

        # Critical Section: Consumer consumes an item from the buffer

        flag[i] = False  # Consumer is out of the critical section

        # Remainder Section: Additional actions after critical section

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(0,))
consumer_thread = threading.Thread(target=consumer, args=(1,))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish
producer_thread.join()
consumer_thread.join()
