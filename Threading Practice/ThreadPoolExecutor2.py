import time
from concurrent.futures import ThreadPoolExecutor


def message(msg, n):
    time.sleep(n)
    print(f"Processing: {format(msg)}")

def main():
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(message, 'message 1', n=3)
        future = executor.submit(message, 'message 2', n=1)

        print("All tasks complete")

if __name__ == "__main__":
    main()

