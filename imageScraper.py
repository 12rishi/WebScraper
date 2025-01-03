from io import BytesIO
import requests
from bs4 import BeautifulSoup
from PIL import Image

search=input("Enter the serach term:")
params={"q":search}
r=requests.get("http://www.bing.com/image/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")
print("beautiful soup is",soup)
links=soup.findAll("a",{"class":"thumb"})
print("all the links are",links)
for item in links:
    img_obj=requests.get(item.attrs["href"])
    print("image object is",img_obj)
    print("getting",item.attrs["href"])
    title=item.attrs["href"].split("/")[-1]
    img=Image.open(BytesIO(img_obj.content))
    print("image content is",img)
    img.save("./scrappedimages/",+title,img.format)


