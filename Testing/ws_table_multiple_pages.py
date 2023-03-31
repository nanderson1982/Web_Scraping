# Import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "http://www.ufcstats.com/statistics/fighters?char=a"
page = requests.get(url)

soup = bs(page.text, 'lxml')

table_body = soup.find('table')

row_data = {}

for i, row in enumerate(table_body.find_all('tr')):
    col = row.find_all('td')
    for ele in col:
        col = ele.text.strip()
        print(col)
        row_data[i] = col
    
print(row_data)