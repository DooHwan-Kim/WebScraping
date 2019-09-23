
import sys
import io
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#로그인 유저정보
LOGIN_INFO = {
    'user_id' : 'outsider7224',
    'user_pw' : '1111111132!!'
}


#Session 생성, with 구분안에서 유지
with requests.Session() as s:
    login_req = s.post('', data=LOGIN_INFO)
    #html 소스확인
    # print('login_req', login_req.text)
    print('login_req', login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one, 'html.parser')
        # print(soup.prettify())
        article = soup.select_one("table:nth-of-type(3)").find_all('p')
        for i in article:
            if i.stirng is not None:
                print(i.string)
