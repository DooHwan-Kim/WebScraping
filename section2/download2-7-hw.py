import sys
import io
import urllib.request as req
import urllib.parse as par
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')

top10 = soup.select("div.hotissue_builtin > div.realtime_part > ol > li > div > div > span.txt_issue > a[tabindex=\"-1\"]")
# li:nth-child(1) > div > div:nth-child(1) > span.txt_issue > a
#print(top10)
for i, e in enumerate(top10, 1):
    print('순위 : {}, 이름 : {}'.format(i, e.string))
