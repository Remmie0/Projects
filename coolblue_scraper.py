#references:
#https://www.youtube.com/watch?v=4VfqVpTz4Q4 by John Watson Rooney for page scraping
#https://www.youtube.com/watch?v=HiOtQMcI5wg By Alex the Analyst for the idea and useful information

from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url_list = []

#Gets the html information of the first page and reads plus cleans it. 
def get_HTML_data(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_all_item_URLs_on_page(soup):
    get_all_item_URLs_on_page.n_add = 0
    #finds all endings of urls of the different laptops on one page
    for url in soup.find_all('a', class_='link' ):

        #to prevent other links from getting in the list
        if url.get('href').startswith('/en/product/'):

            #this is to prevent each link from getting in the list twice
            if url.get('href') not in url_list:
                url_list.append(url.get('href'))
                get_all_item_URLs_on_page.n_add += 1
                

    return url_list

#gets all the items on the starting page and pages after, by default 1
def get_all_items_URLs_on_all_pages(page=1):
    url = 'https://www.coolblue.nl/en/laptops/with-windows-10/processor:intel-core-i7,intel-core-i5,amd-ryzen-7,amd-ryzen-9,intel-core-i9/intern-werkgeheugen-ram:16000000000,32000000000/ingebouwde-camera:ja/schermdiagonaal:0.381-0.40386,0.4064-0.430784,0.4318-0.45466/beeld-definitie-webcams:full-hd-1080p,hd-ready-720p/opslagcapaciteit-van-ssd:512000000000,1000000000000,2000000000000/totale-opslagcapaciteit:1000000000000-1024000000000,1256000000001-,1032000000000/gaming-videokaart:nvidia-geforce-rtx-3050,nvidia-geforce-rtx-3050-ti,nvidia-geforce-rtx-3060,nvidia-geforce-rtx-3060-max-q,nvidia-geforce-rtx-3070,nvidia-geforce-rtx-3070-max-q,nvidia-geforce-rtx-3070-ti,nvidia-geforce-rtx-3070-ti-max-q,nvidia-geforce-rtx-3080,nvidia-geforce-rtx-3080-max-q,nvidia-geforce-rtx-3080-ti,nvidia-geforce-rtx-3080-ti-max-q,nvidia-quadro-rtx-3000,nvidia-quadro-t1000,nvidia-rtx-a2000,nvidia-rtx-a3000?page=1'

    while True:
        #gets the soup of the page
        soup = get_HTML_data(url)

        #gets all the items on the page
        get_all_item_URLs_on_page(soup)

        if page == 1:
            check_next_page = soup.find('a', class_='pagination__link').get('href')
            len_page = len(url_list)
        

        if (page != 1) and (get_all_item_URLs_on_page.n_add == len_page):
            check_next_page = soup.find('a', class_='pagination__link', rel='next').get('href')
       
  
        if check_next_page.startswith('?page='):

            if page + 1 == int(check_next_page[-1:]):
                page = int(check_next_page[-1:])

                print(f'going to page {page}.')

                url = url[:-1] + str(page)

            else: 
                print(f'The url_list has {len(url_list)} items.')
                return url_list
      
                
                

        else:
            print('The function is broken')
            break


get_all_items_URLs_on_all_pages()
