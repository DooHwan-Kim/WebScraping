import sys
import io
import urllib.request as req
import urllib.parse as par
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = par.quote_plus("추천-강좌")

print(quote)

url = base + quote

res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')

print(soup)
