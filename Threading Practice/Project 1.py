from concurrent.futures import ThreadPoolExecutor
import requests

# Use map
# Input:list of URLs
# Task: fetch each URL and return status code + response time
# Workers = 5

def fetch_results(url):
    try:
        response = requests.get(url,timeout=1)
        status_c = response.status_code
        elapsed_time = response.elapsed.total_seconds()
        return url,  status_c, elapsed_time, None

    except Exception as e:
        return url, None, None, str(e)


def main():
    #                   Manual User_Input
    # urls = []
    # while True:
    #     url = input("Enter a URL (# to exit): ")
    #     if url != '#':
    #         urls.append(url)
    #         continue
    #     break

    #                   Testing
    urls = ["https://google.com",
            "https://example.com",
            "http://djssdjjds.co.za"]

    # Sends list of urls, since I have 5 threads each will get its own urls.
    # Using map function, meaning the results will follow the sequence of te input.
    with ThreadPoolExecutor(max_workers=5) as executor:
        responses = executor.map(fetch_results, urls)

        print()
        # Iterating through the results
        for url_response in responses:
            print(url_response)


if __name__ == "__main__":
    main()