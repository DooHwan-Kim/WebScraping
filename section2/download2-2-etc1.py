import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://tvetamovie.pstatic.net/libs/1247/1247167/916dee978108a477733a_20190821204012775.mp4-pBASE-v0-f89364-20190821204100015.mp4"

savepath1 = "c:/test.mp4"

dw.urlretrieve(imgUrl,savepath1)


print('완료')
