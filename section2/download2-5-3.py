from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
from urllib.parse import urljoin

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
inks = soup.find_all("a")
print('inks',type(inks))

for a in inks :
    #print('a value : ', a.attrs['href'])
    txt = a.string
    print('text', txt, '>>href', a.attrs['href'])
