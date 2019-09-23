import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120616_247/cronis1223_1339853552637yJrqx_JPEG/%B5%BF%B9%B0%B9%E8%B0%E6%2811%29.jpg"
htmlURL = "http://google.com"

savepath1 = "c:/test1.jpg"
savepath2 = "c:/index.html"

dw.urlretrieve(imgUrl,savepath1)
dw.urlretrieve(htmlURL,savepath2)


print('완료')
