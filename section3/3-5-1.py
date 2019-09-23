
import sys
import io
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = 'https://www.wishket.com/accounts/login/'
ua = UserAgent()

#Session 생성, with 구분안에서 유지
with requests.Session() as s:
    s.get(URL)
    #로그인 유저정보
    LOGIN_INFO = {
        'identification' : 'makecook',
        'password' : 'Enghks80@!',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']
    }
    # print(s.cookies['csrftoken'])
    login_req = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer' : 'https://www.wishket.com/accounts/login/'})
    # print('login_req', login_req.text)
    # print('login_req', s.headers)

    if login_req.status_code == 200 and login_req.ok:
        soup = BeautifulSoup(login_req.text, 'html.parser')
        # print(soup.prettify())
        projectList = soup.select("table.table-responsive > tbody > tr")
        # print(i.projectList)
        for i in projectList:
            print(i)
            if i.stirng is not None:
                print(i.string)
