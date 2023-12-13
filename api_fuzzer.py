import requests
import sys

wordlist = "common.txt" #change this
url = "https://example.com" #change this
def loop():
    with open(wordlist, 'r') as endpoints:
        for endpoint in endpoints:
            re = requests.get(url=f"{url}/{endpoint}")
            if re.status_code == 404:
                loop()
            else:
                data = re.json()
                print(f"The status code at endpoint {endpoint}: {re.status_code}")
                print(f"The data at endpoint {endpoint} is: {data}")

loop()


