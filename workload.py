import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(number):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def find_sums (numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        executor.map(sum, numbers)


if __name__ == "__main__":
    numbers = [x for x in range(100000000)]
    start_time = time.time()
    find_sums (numbers)
    duration = time.time() - start_time
    print(f"Downloaded {len(numbers)} in {duration} seconds")
