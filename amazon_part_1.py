from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests

def get_data(pageNo):
    ses = HTMLSession()
    URL = 'https://www.amazon.in/s?k=bags&page='+str(pageNo)#+'&crid=2M096C61O4MLT&qid=1679323700&sprefix=ba%2Caps%2C283&ref=sr_pg_'+str(pageNo)
    r = ses.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    for d in soup.find_all('div',attrs={'class':'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right'}):
        name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        url = "https://www.amazon.in" + d.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']
        rating = d.find('span', attrs={'class':'a-size-base'})
        reviews = d.find('span', attrs={'class':'a-size-base s-underline-text'})
        price = d.find('span', attrs={'class':'a-price-whole'})
        bag=[]
        if name is not None:
            bag.append(name.get_text(strip=True))
        else:
            bag.append("unknown-product")
        if url is not None:
            bag.append(url)
        else:    
            bag.append('unknown')
        if rating is not None:
            bag.append(rating.text)
        else:
            bag.append(0)
        if reviews is not None:
            bag.append(reviews.text[1:len(reviews.text)-1])
        else:
            bag.append('0')     
        if price is not None:
            bag.append(price.text)
        else:
            bag.append('0')
    return bag

no_pages = 20
results = []
for i in range(1, no_pages+1):
    results.append(get_data(i))
df = pd.DataFrame(results,columns=['Product Name','URL','Rating','Reviews', 'Price'])
df.to_csv('amazon_products.csv', index=True, encoding='utf-8')