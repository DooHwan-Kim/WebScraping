import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = 'D:/Dropbox/WebScraping/WebScraping/section4/forecast.xml'


if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')


info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    # print(location)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):
        info[loc] = []

    for tmn in weather:
        info[loc].append(tmn.string)
# print(info)

with open('D:/Dropbox/WebScraping/WebScraping/section4/forecast.txt', 'wt',encoding='utf-8') as f:
    for loc in sorted(info.keys()):
        f.write(str(loc) + '\n')
        for n in info[loc]:
            f.write('\t' +str(n) + '\n')
