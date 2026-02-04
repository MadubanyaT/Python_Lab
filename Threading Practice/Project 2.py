from concurrent.futures import ThreadPoolExecutor, as_completed

# File word Counter
# Input: .txt file / Path
# Output: dict {filename: word_count}

def count_words(filepath):
    counter = 0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                counter += len(line.split())

    except Exception as e:
        return {'Filename': filepath, "Words": None, "Error": str(e)}

    return {"Filename": filepath, "Words": counter, "Error": None}


def main():
    file_path = []
    results = []
    file = ''

    while file != "#":
        file = input("Enter file path (# to exit): ")
        if file != "#":
            file_path.append(file)

    # Goal: Take each file assign a threads and do it concurrently
    # Using Submit, is more about getting results fast than in sequential order
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(count_words, f)  for f in file_path] # Takes one at the time

        # Confirming if completed
        for future in as_completed(futures):
            results.append(future.result())

    print()
    for r in results:
        if r["Error"]:
            print(f"File Name: {r['Filename']}; Error: {r['Error']}")
        else:
            print(f"File Name: {r['Filename']}; Words: {r['Words']}")


if __name__ == "__main__":
    main()




