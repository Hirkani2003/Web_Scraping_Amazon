from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

df = pd.read_csv('amazon_products.csv')
def get_data(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    web_page = driver.page_source
    driver.close()
    new_soup = BeautifulSoup(web_page, "html.parser")
    desc = new_soup.find('div', attrs={'class':'a-section a-spacing-medium a-spacing-top-small'})
    details = new_soup.find('ul', attrs={'class':'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list'})
    try:
        manufacturer = details.findAll('li')[2]
        asin = details.findAll('li')[3]
    except:
        print("h")
        manufacturer = None
        asin = None
    product_desc = new_soup.find('div', attrs={'id':'productDescription'})
    bag = []
    if desc is not None:
        bag.append(desc.text)
    else:
        bag.append("unknown")
    if asin is not None:
        bag.append(" ".join(asin.text.split()[4:]))
    else:    
        bag.append('unknown')
    if product_desc is not None:
        bag.append(product_desc.text)
    else:
        bag.append('unknown')
    if manufacturer is not None:
        bag.append(" ".join(manufacturer.text.split()[4:]))
    else:
        bag.append('unknown')
    return bag

results = []
for url in df['URL']:
    results.append(get_data(url))
df_desc = pd.DataFrame(results,columns=['Description', 'ASIN', 'Product Description', 'Manufacturer'])
df_desc.to_csv('amazon_products_description.csv', index=True, encoding='utf-8')
# df_new = pd.concat([df, df_desc], axis=1)
# df_new.to_csv('amazon_products_new.csv', index=True, encoding='utf-8')