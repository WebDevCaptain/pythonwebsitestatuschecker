import requests
import time
import logging
from threading import Thread
from functools import partial

logging.basicConfig(
    level=logging.ERROR,
    filename="logs.txt",
    datefmt="%d-%m-%Y %H:%M:%S",
    format="%(levelname)s  %(asctime)s   [%(message)s]",
)

logger = logging.getLogger("statusChecker")

urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.python.org",
    "https://www.stackoverflow.com",
    "https://www.linkedin.com",
    "https://www.quora.com",
    "https://www.flipkart.com",
    "https://www.medium.com",
]


def make_request(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return logger.error(f"{url} might be down")
        print(f"OK for {url}")
    except:
        logger.error(f"{url} might be down")


while True:
    threads = [Thread(target=partial(make_request, url)) for url in urls]
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Total time taken for the request pool = {time.time() - start}")
    print("Going into hibernation for 5 seconds")
    time.sleep(5)
