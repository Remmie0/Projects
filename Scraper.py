#references:
#https://www.youtube.com/watch?v=4VfqVpTz4Q4 by John Watson Rooney for page scraping
#https://www.youtube.com/watch?v=HiOtQMcI5wg By Alex the Analyst for the idea and useful information

from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.coolblue.nl/en/laptops/with-windows-10/processor:intel-core-i7,intel-core-i5/intern-werkgeheugen-ram:16000000000,32000000000/ingebouwde-camera:ja'

#Gets the html information of the first page and reads plus cleans it. 
def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    pretty_soup = soup.prettify()
    return pretty_soup

print(getdata(url))