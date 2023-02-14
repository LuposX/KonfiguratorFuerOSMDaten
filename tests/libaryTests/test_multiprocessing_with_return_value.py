## Test Multiprocessing
# This file is a minimal use case exmaple of how to use Multiprocessing with return values.
# This will later be used in the project.
# Can be used for example to speed up the calulation of "Vekehrzellen" in the project.

# required imports
import multiprocessing
import time


# this is the function we want to execute, with multiple processes
def worker(x, queue):
    time.sleep(1)
    queue.put(x) # we put the finishes calulated in the queue, late we can get the return value from here


def main():
    # in the queue we will save our return data from the processes
    queue = multiprocessing.SimpleQueue()

    # our tastk, sample data with which we want to start the processes
    tasks = range(10)

    # a list in which we store our created processes
    jobs = []

    # create the processes and start them
    for task in tasks:
        # 'target' is the function we want to start
        p = multiprocessing.Process(target=worker, args=(task, queue,))
        jobs.append(p)  # remember the processes we created
        p.start()

    # wait for the processes to finish calculating and get the output data of all processes
    values = []
    for _ in jobs:
        _.join()  # wait for the process
        values.append(queue.get())

    # print our data
    print(values)



if __name__ == '__main__':
    main()
