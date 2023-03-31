# Import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# Define URL to be scraped
# Add '&page=2' or another number to change page number
# Change 'char=a' to another letter to change tables based on last name
url = "http://www.ufcstats.com/statistics/fighters?char=a"
url_text = requests.get(url).text

# Soup
soup = bs(url_text, 'lxml')
column_headers = soup.find('tr', class_="b-statistics__table-row").text
stats = soup.find_all('td', class_="b-statistics__table-col")
#names = soup.find_all('a', href="http://www.ufcstats.com/fighter-details/93fe7332d16c6ad9")
#print(stats)
table_row = soup.find('tr', class_="b-statistics__table-row")
print(table_row)