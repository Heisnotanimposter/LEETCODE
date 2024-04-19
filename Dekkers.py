def Thread1():
    doWhile=False
    while not completed or not doWhile:
        doWhile=True
        # entry section
        # wait until thread2 is in its critical section
        while (thread2):
            pass

        # indicate thread1 entering its critical section
        thread1 = True

        # critical section

        # exit section
        # indicate thread1 exiting its critical section
        thread1 = False

        # remainder section

def Thread2():
    doWhile=False
    while not completed or not doWhile:
        doWhile=True
        # entry section
        # wait until thread1 is in its critical section
        while (thread1):
            pass

        # indicate thread1 entering its critical section
        thread2 = True

        # critical section

        # exit section
        # indicate thread2 exiting its critical section
        thread2 = False

        # remainder section
        
if __name__ == '__main__':

    # flags to indicate if each thread is in
    # its critical section or not.
    thread1 = False
    thread2 = False

    startThreads()