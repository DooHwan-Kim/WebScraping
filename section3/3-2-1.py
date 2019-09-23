
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


with requests.Session() as s:
    url = 'http://httpbin.org/get'
    headers = {
        'user-agent' : 'myPythonApp_1.0.0'
    }
    r = s.get(url, headers = headers)
    print(r.text)
