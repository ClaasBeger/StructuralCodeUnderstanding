def worker(workernum, barrier):
    # task 1
    sleeptime = random.random()
    print('Starting worker '+str(workernum)+" task 1, sleeptime="+str(sleeptime))
    time.sleep(sleeptime)
    print('Exiting worker'+str(workernum))
    barrier.wait()
    # task 2
    sleeptime = random.random()
    print('Starting worker '+str(workernum)+" task 2, sleeptime="+str(sleeptime))
    time.sleep(sleeptime)
    print('Exiting worker'+str(workernum))


if __name__ == "__main__":
    barrier = threading.Barrier(3)
    w1 = threading.Thread(target=worker, args=((4,barrier)))
    w2 = threading.Thread(target=worker, args=((5,barrier)))
    w3 = threading.Thread(target=worker, args=((6,barrier)))
    w1.start() #START

    w2.start()
    w3.start()

    w1.join()
    w2.join()
    w3.join()