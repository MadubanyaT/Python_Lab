import time
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor



def task(n):
    print(f"Task {n} is starting.")
    time.sleep(n)
    print(f'Task {n} is complete.')
    return n

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:     # max_workers => Number of threads created
        results = executor.map(task, [2, 6, 1, 5]) # maps() assigns those 3 threads tasks to handle, in this case
                                                            #  random number to handle. Results are returned in order


        # futures = [executor.submit(task, item) for item in range(1,6)]
        # results = [f.result() for f in futures]
        #  executor.submit() => Returns a future as a result

        #  as_completed() => returns the result that is complete not order

        print("Results: ", list(results))
        print("Main thread finished.")


if __name__ == "__main__":
    main()
