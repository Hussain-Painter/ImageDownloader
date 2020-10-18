from bs4 import BeautifulSoup
import requests as rq
from PIL import Image
from io import BytesIO
import os

def startSearch():
    search = input("Enter something to be searched: ") #Asking for input
    dir_name = search.replace(" ","_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    params = {"q": search} #initialising params
    r = rq.get("https://www.bing.com/images/search", params=params) #using request.get
    soup = BeautifulSoup(r.text, "html.parser") #using Beautiful Soup to parse text
    links = soup.findAll("a", {"class": "thumb"})
    i = 1
    for link in links:
        try:
            img_obj = rq.get(link.attrs["href"])
            print("Getting", link.attrs["href"])
            try:
                img = Image.open(BytesIO(img_obj.content))
                title = link.attrs["href"].split("/")[-1]
                img.save("./"+dir_name+"/"+title+".", img.format)

            except:
                print("Could not save")
        except:
            print(("Could not request"))
    cont = input("Do you want to continue? Type yes or no? ")
    if cont.lower() == "yes" or "y":
        startSearch()
    else:
        return

startSearch()