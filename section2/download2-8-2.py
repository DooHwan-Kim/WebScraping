import sys
import io
import os
import urllib.request as req
import urllib.parse as par
from bs4 import BeautifulSoup



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = par.quote_plus("사자")

#print(quote)

url = base + quote

res = req.urlopen(url).read()
savePath = "C:\\imagedown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise
soup = BeautifulSoup(res,'html.parser')
img_list = soup.select("div.photo_grid._box > div > a.thumb._thumb > img ")
#print(img_list)
for i, img_list in enumerate(img_list, 1):
    #print(i, img_list["data-source"])
    fulFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(img_list["data-source"], fulFileName)
