import requests
from bs4 import BeautifulSoup

def get_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article")

    for book in books:
        title = book.find("h3").find("a")["title"]
        rating = book.p["class"][1]
        print(f"The book name is {title} and its rating is {rating} starts")

# Usage
get_book_info("https://books.toscrape.com/")