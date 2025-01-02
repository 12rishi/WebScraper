import bs4.element
from bs4 import BeautifulSoup
import requests
search=input("enter the search query")
params={"q":search}
r=requests.get("http://www.bing.com/search",params=params)
print(r.status_code)
soup=BeautifulSoup(r.text,"html.parser")
print(type(soup.prettify()))
results=soup.find("ol",{"id":"b_results"})
lists=results.findAll("li")
for item in lists:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]
    children=item.find("h2")
    print("next sibling of h2 is",children.next_sibling.find("p",{"class":"b_lineclamp2"}))
