from bs4 import BeautifulSoup, Comment
import sys
import io
import re
import urllib.request as req
from urllib.parse import urlencode
from math  import ceil
import openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def gettcount(inputdata):
    p = re.compile('총? *\d+구?좌권? *\d*매? *[([]')
    tdata = p.findall(inputdata)

    if len(tdata) != 0:
        rowlist = tdata[0].replace(" ","").strip().split('좌')
    else:
        return 0

    nump = re.compile('\d*')
    rcou = 1
    for e in rowlist:
        e = ''.join(nump.findall(e))
        if e == '':
            n = 1
        else:
            n = int(e)
        rcou *= n
        #print('e', e, 'n', n)

    return rcou

def getscount(inputdata):
    inputdata = inputdata.replace("-","~").replace(",","~")
    if inputdata.count('~') > 0:
        rowlist = inputdata.split('~')
        nump = re.compile('\d*')
        fristdata = ''.join(nump.findall(rowlist[0])).strip()
        seconddata =  ''.join(nump.findall(rowlist[1])).strip()
        fl = len(fristdata)
        sl = len(seconddata)

        if fl != sl:
            seconddata = fristdata[0:(fl-sl)] + seconddata

        fristdata = int(fristdata)
        seconddata = int(seconddata)
        if seconddata - fristdata > 0:
            return seconddata - fristdata + 1
        else:
            return 0
    elif inputdata.strip() == '':
        return 0
    else:
        return 1

def getscountr(inputdata):
    if inputdata.count("전문건설공제조합") > 0:
        sidx = inputdata.index("전문건설공제조합") + 8
        inputdata = inputdata[sidx:]

    p1 = re.compile('가제? *\d+[~-]?가?제?\d*호?')
    p5 = re.compile('나제? *\d+[~-]?나?제?\d*호?')
    p10 = re.compile('다제? *?\d+[~-]?다?제?\d*호?')
    p15 = re.compile('라제? *\d+[~-]?라?제?\d*호?')
    p30 = re.compile('마제? *\d+[~-]?마?제?\d*호?')
    p50 = re.compile('바제? *\d+[~-]?바?제?\d*호?')

    p1e = p1.findall(inputdata)
    p5e = p5.findall(inputdata)
    p10e = p10.findall(inputdata)
    p15e = p15.findall(inputdata)
    p30e = p30.findall(inputdata)
    p50e = p50.findall(inputdata)

    scoun = 0
    for m in p1e:
        scoun += getscount(m) * 1
    for m in p5e:
        scoun += getscount(m) * 5
    for m in p10e:
        scoun += getscount(m) * 10
    for m in p15e:
        scoun += getscount(m) * 15
    for m in p30e:
        scoun += getscount(m) * 30
    for m in p50e:
        scoun += getscount(m) * 50

    #print('i', i, e, 'scoun', scoun)
    return scoun

def getparam(pageNum):
    values = {
          "w" : "bid"
        , "pg" : str(pageNum)
        , "outmax" : "50"
        , "section" : ""
        , "q1" : "전문건설공제조합"
        , "q2" : ""
        , "q3" : ""
        , "msort" : "d:4:1,d:5:1,d:17:1,d:18:1"
        , "grouppart" : ""
        , "groupcd" : ""
        , "part" : ""
        , "detailCheck" : "on"
        , "gnbSiDo" : ""
        , "gnbSiGunGu1" : ""
        , "gnbSiGunGu2" : ""
        , "gnbSiGunGu3" : ""
        , "gnbSiDoCd" : ""
        , "gnbSiGunGuCd1" : ""
        , "gnbSiGunGuCd2" : ""
        , "gnbSiGunGuCd3" : ""
        , "detailType" : "0004"
        , "dpslMtdCd1" : ""
        , "dpslMtdCd2" : ""
        , "dpslMtdCd3" : ""
        , "prptDvsnNm" : ""
        , "prptDvsnCd" : ""
        , "collateralGbnCd" : ""
        , "ctgrName" : ""
        , "ctgrId1" : ""
        , "ctgrId2" : ""
        , "ctgrId3" : ""
        , "ctgrCd1" : ""
        , "ctgrCd2" : ""
        , "ctgrCd3" : ""
        , "addrName" : ""
        , "addrType" : "road"
        , "siDo" : ""
        , "siGunGu" : ""
        , "emd" : ""
        , "siDoCd" : ""
        , "siGunGuCd" : ""
        , "emdCd" : ""
        , "dtmType" : "d4"
        , "dtmName" : ""
        , "dtmBegin" : "2017-01-01"
        , "dtmCls" : "2019-08-31"
        , "orgNm" : ""
        , "monType" : ""
        , "begnMon" : ""
        , "clsMon" : ""
        , "maxMon" : ""
        , "sqmsType" : ""
        , "sqmsFrom" : ""
        , "sqmsTo" : ""
        , "bidResult" : "10"
        , "publicType" : ""
    }
    return urlencode(values).encode('utf-8')


def gettotal():
    url = "http://www.onbid.co.kr/search/int/bid.do"
    post_data = getparam(1)
    urlWithPost = req.Request(url, post_data)
    reqData = req.urlopen(urlWithPost).read().decode('utf-8')
    soup = BeautifulSoup(reqData, "html.parser")
    totalcou = soup.select_one("._w_totcnt").string
    try:
        if type(totalcou) != '<class \'str\'>':
            return int(str(totalcou).replace(",", ""))
        else:
            return int(totalcou.replace(",", ""))
    except:
        return -1

def getlist(pageNum, onbidlist):
    url = "http://www.onbid.co.kr/search/int/bid.do"
    post_data = getparam(pageNum)
    urlWithPost = req.Request(url, post_data)
    reqData = req.urlopen(urlWithPost).read().decode('utf-8')
    soup = BeautifulSoup(reqData, "html.parser")

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
       comment.extract()

    data = soup.select("table.op_tbl_type1 > tbody > tr")

    #주석 제거

    for i, e in enumerate(data):

        while(e.select_one("dd").em != None):
            e.select_one("dd").em.unwrap()

        e.select_one("td:nth-child(6)").br.unwrap()
        itemNo = e.select_one("a").string
        itemNm = ''.join(e.select_one("dd").contents)
        itemType = e.select("dd")[1].contents[0].strip()
        gamt = str(e.select_one("span").string).strip()
        #print('iso', i, e.select_one("span:nth-of-type(2)").string)
        amt = e.select("span")[1].contents[1].strip()
        datedt = ' '.join(e.select_one("td:nth-child(6)").contents)

        onbidlist.append({
            "물건관리번호" : itemNo,
            "물건명" : itemNm,
            "물건종류" : itemType,
            "예상가" : gamt,
            "낙찰가" : amt,
            "개찰일시" : datedt
        })

def saveexcel(filepath, onbidlist):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'onbid낙찰정보'
    sheet.append(list(onbidlist[0].keys()))
    for e in onbidlist:
        # print(e)
        sheet.append(list(e.values()))
    wb.save(filepath)


totalrow = gettotal()
n = ceil(totalrow/50)
print('totalrow', totalrow, 'maxpage', n)
onbidlist=[]

for i in range(1,n+1):
    getlist(i,onbidlist)

# getlist(1,onbidlist)

for e in onbidlist:
    tcount = gettcount(e["물건명"])
    scount = getscountr(e["물건명"])
    gamt = int(e["예상가"].replace(",",""))
    amt = int(e["낙찰가"].replace(",",""))

    if tcount == 0:
        gavg1 = None
        avg1 = None
    else:
        gavg1 = gamt / tcount
        avg1 = amt / tcount

    if scount == 0:
        gavg2 = None
        avg2 = None
    else:
        gavg2 = gamt / scount
        avg2 = amt / scount

    e["좌수1"] = tcount
    e["좌수2"] = scount
    e["예상가평균1"] = gavg1
    e["예상가평균2"] = gavg2
    e["낙찰가평균1"] = avg1
    e["낙찰가평균2"] = avg2

saveexcel('c:\\test.xlsx', onbidlist)

print(onbidlist)
