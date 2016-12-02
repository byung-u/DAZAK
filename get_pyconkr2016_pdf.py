#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import telepot

from requests import get
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = "https://github.com/pythonkr/pyconapac-2016-files"
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in  soup.find_all('a'):
        repo = link.get('href')
        if (repo.endswith('.pdf')):
            pdf_url = 'https://github.com%s' % (repo)
            print(pdf_url)

    sys.exit(0)
