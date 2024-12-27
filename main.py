from bs4 import BeautifulSoup
import requests
search=input("enter the search query")
params={"q":search}
r=requests.get("https://www.tripadvisor.com/Restaurants-g293890-c31-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html",params=params)
print(r.status_code)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
