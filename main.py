from bs4 import BeautifulSoup
import urllib.parse
from requests_html import HTMLSession

s = HTMLSession()

url = 'https://sa.aqar.fm/%D8%B4%D9%82%D9%82-%D9%84%D9%84%D8%A5%D9%8A%D8%AC%D8%A7%D8%B1/%D8%AC%D8%AF%D8%A9/%D8%B4%D9%85%D8%A7%D9%84-%D8%AC%D8%AF%D8%A9/1'

global num
num = 0

def pagesearch(url):
    htmltext = s.get(url).text
    soup = BeautifulSoup(htmltext, "lxml")
    listings = soup.find_all("div", class_="listItem")

    for listing in listings:

        location = listing.find("a", class_="listTitle").text
        print(location[14:(len(location) - 6)].replace(" ، ", " - "))

        try:
            price = listing.find("span", class_="price").text
            print(price)
        except AttributeError:
            print("Apartment price not declared")

        try:
            size = listing.find("span", class_="size").text
            print(size)
        except AttributeError:
            print("Apartment size not declared")

        try:
            bedrooms = listing.find("span", class_="bed").text
            print(bedrooms + "bedrooms")
        except AttributeError:
            print("Number of bedrooms not declared")
        try:
            bathrooms = listing.find("span", class_="bath").text
            print(bathrooms + "bathrooms")
        except AttributeError:
            print("Number of bathrooms not declared")


        link = listing.find("a", class_="listTitle")['href']
        print("https://sa.aqar.fm" + urllib.parse.quote(link))

        global num
        num = num + 1
        print(num)
        print("--------------------")

    return soup

def nextpageee(soup):
    nextpage = soup.find("ul", class_="paging")
    if nextpage.find('a', id ="next-page"):
        endcodeurl = nextpage.find('a', rel ="next")['href']
        url = "https://sa.aqar.fm" + urllib.parse.quote(endcodeurl)
        return url
    else:
        return

while True:
    data = pagesearch(url)
    url = nextpageee(data)
    if not url:
        break










