# Web Scraping Amazon for Bags using Python, BeautifulSoup4, and Selenium

This project demonstrates how to web scrape Amazon's search results for bags using Python, BeautifulSoup4, and Selenium.

The script will automate the process of navigating through 20 pages of search results for a given search term and extract the following information for each product:  

Part 1 :
* Product URL
* Product Name
* Product Price
* Rating
* Number of reviews  
Part 2:  
With the Product URL received in the above case, hit each URL, and add below items:
* Description
* ASIN
* Product Description
* Manufacturer

## Installation

Python 3.6+
BeautifulSoup4
Selenium
You can install these packages using pip:

```bash
pip install beautifulsoup4
pip install selenium
```

## Usage
To use this script, simply clone this repository and run the amazon_part_1.py and amazon_part_2.py file with Python.
```bash
python scrape_amazon.py
```
The script will open a Chrome browser and navigate to the Amazon search results page for the given search term. It will then extract the information for each product on each page of results and save it to a CSV file named amazon_products.csv and amazon_products_description.csv.

## Clickable URLs
To make the product URLs clickable in the CSV file, you can use the `=HYPERLINK()` formula in Excel.

1. Open the `amazon_products.csv` file in Excel.  
2. Select the column containing the product URLs.  
2. Click the `Insert` tab at the top of the screen.   
4. Click the `Function` button in the toolbar.  
5. In the `Select a Function` box, select `HYPERLINK`.  
6. In the `Location` box, select the first cell containing the product URL.  
7. In the `Friendly Name` box, enter a descriptive name for the link (e.g. "View Product").  
8. Click `OK`.  
9. The product URL will now be clickable in the spreadsheet.  
