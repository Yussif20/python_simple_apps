import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

soup=BeautifulSoup(response.content,"html.parser")

books=soup.find_all("article")

for book in books:
    title=(book.find("h3").find("a")["title"])
    rating=(book.p["class"][1])
    print(f"The book name is {title} and its rating is {rating} starts")

