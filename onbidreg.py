import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

datalist = [
    #   "경기도 부천시 심곡동 355-1 전문건설공제조합 부천지점(태원건설(주) 출자증권:가제13912,나제5028,다제8194,다제16893,라제7190,바제16958)"
    # , "경기도 성남시 분당구 정자동 25-1 전문건설공제조합 출자증권 2좌(1좌권:가제102139호, 가제102142호)"
    # , "경기도 이천시 중리동 486 이천세무서 보관 [전문건설공제조합 츨자증권 10좌권 1매(다제34670호)]"
    # , "부산광역시 부산진구 범천동 853-40 전문건설공제조합(부산지점) 출자증권 36좌(30좌권:마제036813호, 5좌권:나제011733호, 1좌권:가제229328호)"
    # , "충청북도 청주시 상당구 용암동 1700 전문건설공제조합 출자증권 총 17좌(10좌권 1매:다007019호,1좌권 7매: 가016444~5호,가017563호,가012056~012059호)"
    # , "서울특별시 강남구 역삼동 824 삼성세무서 법인납세1과에 보관중인 전문건설공제조합 출자증권 10좌(10좌권 1매: 다제046934호)"
    # , "서울특별시 동작구 신대방동 395-70 전문건설공제조합 출자증권 총 40좌 (1좌 10매 : 가제 098220~3호,가제 030882~3호,가제 065398~9호,가제 076481호,가제 081899호,15좌권 2매 : 라제 013537호,라제 004440호)"
    # , "충청북도 청주시 상당구 용암동 1700 전문건설공제조합 출자증권 12좌[10좌권1매:다055062호 ,1좌권2매:가175545호 ,가240593호 ]"
    # , "대전광역시 서구 둔산동 1290 8층 전문건설공제조합 대전지점 출자증권 20좌(10좌권: 다제47918호, 다제47919호)"
    # , "충청남도 예산군 예산읍 산성리 784 전문건설공제조합 예산지점 출자증권 31좌(1좌권: 가제223191호, 30좌권: 마제32382호)"
    # , "충청남도 예산군 예산읍 산성리 784 전문건설공제조합 예산지점 [1좌권 : 가제140713~5호, 5좌권 : 나제048988호, 15좌권 : 라제012388호]"
    # , "경기도 부천시 심곡동 355-1 성보빌딩 9층 전문건설공제조합 부천지점((주)일심석재 출자증권:가제110030,가제110031,가제110032,가제110033,가제110034,가제110035,다제55129)"
    # , "경상북도 포항시 북구 덕산동 121-2 북구청 내 전문건설공제조합출자증권 총2좌 [ 일좌권2매(가제145939호,가제216805호) ]"
    # , "경상북도 포항시 북구 덕산동 121-2 북구청 내 전문건설공제조합출자증권 총3좌 [ 일좌권3매(가제67189호~67191호) ]"
    # , "부산광역시 부산진구 범천동 853-40 전문건설회관빌딩 (9층) 전문건설공제조합 출자증권 112좌[바제14194,45602호 ,나제50170호 ,가제227159,227166~8,227172~3,231078호 ]"
    # , "경상북도 구미시 공단동 174 구미세무서 내 전문건설공제조합출자증권 총18좌 [ 일좌권3매(가제224610~224612호) ,오좌권1매(나제48175호) ,일십좌권1매(다제57052호) ]"
    # , "서울특별시 영등포구 영등포동4가 57 전문건설공제조합 영등포지점((주)장극토건 출자증권:다제12758)"
    # , "부산광역시 부산진구 범천동 853-40 전문건설공제조합 부산지점 출자증권 117좌(1좌권(가제071537~8, 055168~9, 061412~4호 7매), 10좌권(다제022184, 022188, 025096~7, 000767, 002398, 011544, 011672, 013039, 014741, 016727호 11매)]"
    # , "대구광역시 남구 대명동 1593-20 남대구세무서 내 전문건설공제조합출자증권 총35좌 [ 오좌권1매(나제55065호) ,삼십좌권1매(마제36216호) ]"
    # , "충청북도 청주시 상당구 용암동 1700 전문건설공제조합 출자증권 51좌[50좌권 1매:바005980호 ,1좌권 1매:가231760호 ]"
    # , "대구광역시 동구 신암동 36-1 동구청 내 전문건설공제조합출자증권 총4좌 [ 일좌권4매(가제119169~119170호,가제241831~241832호) ]"
    # , "충청북도 청주시 상당구 용암동 1700 전문건설공제조합 출자증권 19좌[10좌권 1매:다036452호 ,5좌권 1매:나018066호 ,1좌권 4매:가126627~9호 ,가065451호 ]"
     "서울특별시 동작구 신대방동 395-70 [전문건설공제조합 출자증권 총45좌 / 1좌권(가제085164, 092555, 092556, 092557, 116519), 5좌권(나제008569, 017963), 30좌권(마제003772)] "
    # , "전라북도 전주시 덕진구 인후동2가 1530-15 전문건설공제조합 전주지점 [ 1좌권 : 가제127386호, 가제240511~6호]"
    # , "전라북도 전주시 덕진구 인후동2가 1530-15 전문건설공제조합 전주지점[1좌권 : 가제215717~8호, 10좌권 : 다제53550호]"
]


def gettcount(inputdata):
    p = re.compile('총? *\d+구?좌권? *\d*매? *[([:/]')
    tdata = p.findall(inputdata)
    print(tdata)
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

print(gettcount(datalist[0]))

# def getscount(inputdata):
#     inputdata = inputdata.replace("-","~").replace(",","~")
#     if inputdata.count('~') > 0:
#         rowlist = inputdata.split('~')
#         nump = re.compile('\d*')
#         fristdata = ''.join(nump.findall(rowlist[0])).strip()
#         seconddata =  ''.join(nump.findall(rowlist[1])).strip()
#         fl = len(fristdata)
#         sl = len(seconddata)
#
#         if fl != sl:
#             seconddata = fristdata[0:(fl-sl)] + seconddata
#
#         fristdata = int(fristdata)
#         seconddata = int(seconddata)
#         if seconddata - fristdata > 0:
#             return seconddata - fristdata + 1
#         else:
#             return 0
#     elif inputdata.strip() == '':
#         return 0
#     else:
#         return 1
#
# def getscountr(inputdata):
#
#     if inputdata.count("전문건설공제조합") > 0:
#         sidx = inputdata.index("전문건설공제조합") + 8
#         inputdata = inputdata[sidx:]
#
#     p1 = re.compile('가제? *\d+[~-]?가?제?\d*호?')
#     p5 = re.compile('나제? *\d+[~-]?나?제?\d*호?')
#     p10 = re.compile('다제? *?\d+[~-]?다?제?\d*호?')
#     p15 = re.compile('라제? *\d+[~-]?라?제?\d*호?')
#     p30 = re.compile('마제? *\d+[~-]?마?제?\d*호?')
#     p50 = re.compile('바제? *\d+[~-]?바?제?\d*호?')
#
#     p1e = p1.findall(inputdata)
#     p5e = p5.findall(inputdata)
#     p10e = p10.findall(inputdata)
#     p15e = p15.findall(inputdata)
#     p30e = p30.findall(inputdata)
#     p50e = p50.findall(inputdata)
#
#     scoun = 0
#     for m in p1e:
#         scoun += getscount(m) * 1
#         print('m', m, getscount(m))
#     for m in p5e:
#         scoun += getscount(m) * 5
#     for m in p10e:
#         scoun += getscount(m) * 10
#     for m in p15e:
#         scoun += getscount(m) * 15
#     for m in p30e:
#         scoun += getscount(m) * 30
#     for m in p50e:
#         scoun += getscount(m) * 50
#
#     #print('i', i, e, 'scoun', scoun)
#     return scoun
#
# for i, e in enumerate(datalist):
#     print('i', i, getscountr(e), 'e', e)
