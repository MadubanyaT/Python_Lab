import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import os



# numbers = [3, 1, 2]
#
# def work(n):
#     time.sleep(n)
#     return  n
#
#
# def main():
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         results = executor.map(work, numbers)
#
#         for r in results:
#             print(r) # 3 1 2: because map returns results in sequential order

def read_size(file, n):
    time.sleep(n)
    try:
        size = os.path.getsize(file)
    except Exception as e:
        return file, None, str(e)

    return  file, size, None


def main():
    file_paths = []
    results = []

    while True:
        file_path = input("Enter file path (# to exit): ")
        if file == '#':
            break
        file_paths.append(file)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(read_size, f, 1) for f in file_paths]

        for future in as_completed(futures):
            results.append(future.result())

    for r in results:
        if r[2] is None:
            print(f"{r[0]}, {r[1]} kb")
        else:
            print(f"{r[0]}, {r[2]}")

if __name__ == "__main__":
    main()
