#-*-coding:UTF-8 -*-
# 使用 BeautifulSoup 4 parser 網頁
# https://www.crummy.com/software/BeautifulSoup/#Download
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import urllib2

# https://gas.goodlife.tw/
url = "https://gas.goodlife.tw/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Charset': 'utf-8,ISO-8859-1;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
       'Connection': 'keep-alive'}
req = urllib2.Request(url, headers=hdr)
response = urllib2.urlopen(req)
html = response.read()
#print(html)
#parser.feed(html)
soup = BeautifulSoup(html, 'html.parser')
print("==== start ====")
for element in soup.find_all('div',id="gas-price"):
	for item in element.find_all('h2'):
		print(item.get_text().strip())		
print("==== end ====")