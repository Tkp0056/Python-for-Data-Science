# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:14:29 2022

@author: acer
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} -requests.get('url',headers=headers).text

requests.get('https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1')
