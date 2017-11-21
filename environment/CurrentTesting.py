#
# Web Scraper
# Version: 5

"""
cd C:\Users\Dexter Carpenter\Documents\GitHub\WebScraper\environment

c:\Python27\Scripts\virtualenv.exe -p C:\Python27\python.exe .lpvenv

.lpvenv\Scripts\activate

# on at home computer:

cd C:\Users\dexte\Documents\GitHub\WebScraper\environment

"""

# import libraries
import urllib2
from bs4 import BeautifulSoup as BS
import time

#variables
global tagcount

print ""
print "Press 'Ctrl + C' to exit the program"
# specify the url
quote_page = raw_input('Enter what website you want to scrape:')
print ""

"""
def main():
    # specify the url
    quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

    # query the website and return the html to the variable page
    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soap and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'name'})

    name = name_box.text.strip() # strip() is used to remove starting and trailing
    print name

    # get the index price
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text
    print price
"""


def scraper():
    # query the website and return the html to the variable page
    page = urllib2.urlopen(quote_page)
    
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BS(page, 'html.parser')
    
    #find number of tags
	soup = BS(html)
    return len(soup.find_all(tag_name))
	
	
    print tagcount
    
    # get the index price
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text
    print price

while True:
    
    if __name__ == "__main__":
        scraper()
    
    time.sleep(10)
    
    tagcount = 0

























"""
Nathan Says this is trash -- it is for printing to an excel file?......

import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])

quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']

# for loop
data = []
for pg in quote_page:
 # query the website and return the html to the variable page
 page = urllib2.urlopen(pg)
# parse the html using beautiful soap and store in variable 'soup'
 soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
 name_box = soup.find('h1', attrs={'class': 'name'})
 name = name_box.text.strip() # strip() is used to remove starting and trailing
# get the index price
 price_box = soup.find('div', attrs={'class':'price'})
 price = price_box.text
# save the data in tuple
 data.append((name, price))

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 # The for loop
 for name, price in data:
    writer.writerow([name, price, datetime.now()])
"""




