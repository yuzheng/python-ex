#-*-coding:UTF-8 -*-
# 使用 BeautifulSoup 4 parser 網頁
# https://www.crummy.com/software/BeautifulSoup/#Download
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# ex: python parserPlay.py com.fitel.tabata
# ex: python parserPlay.py com.chttl.ubi
# ex: python parserPlay.py -l zh_TW -p softwareVersion com.chttl.ubi
from bs4 import BeautifulSoup
import urllib2
import getopt,sys

#getopt.getopt ( [命令行參數列表], '短選項', [長選項列表] )
#短選項名後的冒號:表示該選項必須有附加的參數
#長選項名後的等號=表示該選項必須有附加的參數
#返回opts和args 
try:
	opts, args = getopt.getopt(sys.argv[1:], 'l:p:', ["hl=", "itemprop="])
except getopt.GetoptError as err:
	# print help information and exit:
	print(err) # will print something like "option -a not recognized"
	sys.exit(2)
#print(opts)
#print(args)
hl = "zh_TW"
itemprop = "";
for o, a in opts:
	if o in ("-l", "--hl"):
		hl = a
	elif o in ("-p", "--itemprop"):
		itemprop = a
	else:
		assert False, "unhandled option"

if len(args) == 0:
	print("ERROR, please input app id.")
else:
	print(args)
	#https://play.google.com/store/apps/details?id=XXX&hl=zh_TW
	host = "https://play.google.com/store/apps/details"
	app = args[0]	
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	       'Accept-Charset': 'utf-8,ISO-8859-1;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
	       'Connection': 'keep-alive'}
	url = "%s?id=%s&hl=%s"%(host,app,hl)
	print(url)
	req = urllib2.Request(url, headers=hdr)
	response = urllib2.urlopen(req)
	html = response.read()
	#print(html)
	#parser.feed(html)
	soup = BeautifulSoup(html, 'html.parser')
	print("==== start ====")
	#for element in soup.find_all('div',class_="content"):
	for element in soup.find_all('div',attrs={"itemprop": True}): #itemprop="datePublished"
		if(len(itemprop)==0 or (len(itemprop)>0 and element['itemprop']==itemprop)):
			print(element['itemprop'])
			print(element.get_text().strip())		
	print("==== end ====")