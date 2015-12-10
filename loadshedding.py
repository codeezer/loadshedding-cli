#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://myrepublica.com/load-shedding.html')
soup = BeautifulSoup(r.text,'html.parser')
rows = soup.find_all('tr')
table = []
for each_row in rows:
    columns = each_row.find_all('td')
    columns = [ele.text.strip() for ele in columns]
    table.append([ele for ele in columns if ele])


for data in table:
    for row in data:
        print(row,end='\t')
    print('\n')
