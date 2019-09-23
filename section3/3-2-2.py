
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


with requests.Session() as s:
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    r = s.get(url)
    print(r.json().keys())
    print(r.json().values())
    print(r.encoding)
