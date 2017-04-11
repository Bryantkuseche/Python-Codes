# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:35:52 2017

@author: bryan
"""

from bs4 import BeautifulSoup as Soup
import urllib
import re

url = 'http://www.formula1.com'
html = urllib.urlopen(url)
sopa = Soup(html , 'html.parser')
for link in sopa:
    print link
