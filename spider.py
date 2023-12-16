#https://en.m.wikipedia.org/wiki/Programmer
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


visited_urls = set()

def spider_urls(url, keyword):
    try:
        res = requests.get(url)
    except:
        print(f"Request failed {url}")
        return
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        for u in urls:
            if u not in visited_urls:
                visited_urls.add(u)
                url_join = urljoin(url, u)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass


url = input("Enter the url you want to scrap: ")
keyword = input("Enter the keyword you search for the URL you provided: ")
spider_urls(url, keyword)