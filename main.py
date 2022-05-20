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
    jobs = soup.find_all("div", class_="listItem")

    for job in jobs:
        try:
            location = job.find("a", class_="listTitle").text
            price = job.find("span", class_="price").text
            size = job.find("span", class_="size").text
            bedrooms = job.find("span", class_="bed").text
            bathrooms = job.find("span", class_="bath").text
            link = job.find("a", class_="listTitle")['href']
            print(location[14:(len(location)-6)].replace(" ، ", " - "))
            print(price)
            print(size)
            print(bedrooms + "bedrooms")
            print(bathrooms + "bathrooms")
            print("https://sa.aqar.fm" + urllib.parse.quote(link))
        except AttributeError:
            print("No data available")


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










