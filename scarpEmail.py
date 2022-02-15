import requests
import bs4
import lxml

url='http://www.publicdial.com/free-bulk-email-id-list100to105K.aspx'
dic={
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Cookie": "ASP.NET_SessionId=yu3gsbkzcg3xcs5rdgp1apyi",
"Host": "www.publicdial.com",
"Pragma": "no-cache",
"Referer": "http://www.publicdial.com/free-bulk-email-id-list100to105K.aspx",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
r=requests.post(headers=dic, url=url, allow_redirects=True)

soup=bs4.BeautifulSoup(r.text,'lxml')
trs=soup.find_all('tr')
# print(trs)
table=soup.find_all('table',{'id':'ctl00_MainContent_dlAdPost'})
val=[]
for ta in table:
	ts=ta.find_all('tr')
	tt=ta.find_all('td')
for ut in tt:
 	l=ut.text.strip()
 	listt=[l]
 	val.append(listt)
 	print(val)

	






