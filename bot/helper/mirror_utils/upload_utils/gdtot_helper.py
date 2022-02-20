import sys
import os
import requests as rq
import re
import json as js
from bs4 import BeautifulSoup as bt
import random
from bot import GDTOT_COOKIES


def cookie_checker():
    """added support to use many GDtot cookies to Bypass limit"""
    GDTOT_COOKIES_SET = set()
    try:
        a_gdtot_cookies = GDTOT_COOKIES.split("||")
        for cookie in a_gdtot_cookies:
            GDTOT_COOKIES_SET.add(str(cookie))
        GDTOT_COOKIES_LIST = list(GDTOT_COOKIES_SET)
        return {"cookie": random.choice(GDTOT_COOKIES_LIST)}
    except:
        return ""

class GDTOT:
      def __init__(self):
          self.r = 'https://new.gdtot.top/'
          self.COOKIES = cookie_checker()
          self.c = GDTOT.check(self)
          self.h = {
                   'upgrade-insecure-requests': '1',
                   'save-data': 'on',
                   'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Dual) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-dest': 'document',
                   'referer': self.r,
                   'prefetchAd_3621940': 'true',
                   'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
                   }

      def check(self):
          """Check cookies and Ready it for work"""
          try:
              j = js.loads(js.dumps(self.COOKIES))['cookie'].replace('=',': ').replace(';',',')
              f = re.sub(r'([a-zA-Z_0-9.%]+)', r'"\1"', "{%s}" %j)
              c = js.loads(f)
              return c
          except Exception as e:
              print(e)
              return ""

      def parse(self, url):
          """Main function to get the URL"""
          if url == "":
              return
          if self.c == "":
              print("Please provide cookies")
              return
          else:
             try:
                 r1 = rq.get(url, headers=self.h, cookies=self.c).content
                 p = bt(r1, 'html.parser').find('button', id="down").get('onclick').split("'")[1]
                 self.r = url
                 r2 = bt(rq.get(p, headers=self.h, cookies=self.c).content, 'html.parser').find('meta').get('content').split('=',1)[1]
                 self.r = p
                 r3 = bt(rq.get(r2, headers=self.h, cookies=self.c).content, 'html.parser').find('div', align="center")
                 if r3 == None:
                    r3 = bt(rq.get(r2, headers=self.h, cookies=self.c).content, 'html.parser')
                    f = r3.find('h4').text
                    return 404, f
                 else:
                    s = r3.find('h6').text
                    i = r3.find('a', class_="btn btn-outline-light btn-user font-weight-bold").get('href')
                    return s,i
             except Exception as e:
                 print(e)
                 return 404, 404
