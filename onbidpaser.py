import sys
import io
import re
from bs4 import BeautifulSoup, Comment

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = '''
<tr>
<td class="al">
<div class="info_wrap pl5">
<dl class="info w270 ml0">
<dt><a href="/op/cta/cltrdtl/collateralDetailMoveableAssetsDetail.do?cltrHstrNo=3174117&amp;cltrNo=1357675&amp;plnmNo=548180&amp;pbctNo=9421704&amp;scrnGrpCd=0006&amp;pbctCdtnNo=3234177" target="_blank">2019-07705-001</a></dt>
<dd>경기도 부천시 심곡동 355-1 전문건설공제조합 부천지점(태원건설(주) 출자증권:가제13912,나제5028,다제8194,다제16893,라제7190,바제16958)</dd>
<dd class="tpoint_03">

										[유가증권/유가증권(주식, 채권 등)]</dd>
<dd>
</dd>
</dl>
</div>
</td>
<td class="ar">
<span>

			           		 75,967,000</span>
</td>
<td class="ar">
<span> <!-- 20151006 입찰금액공개여부가 Y일경우만 낙찰가 공개 -->

83,267,000</span>
</td><!-- 20150729 클래스명 삭제 --> <!-- 201507803 텍스트 수정 -->
<td>
<span><!-- 20151006 입찰금액공개여부가 Y일경우만 낙찰율 공개 -->

109.61 %</span>
</td><!-- 20150729 클래스명 삭제 -->
<td>
<!--2016.04.11 물건상태표시 F_PBCT_STAT_NM 참고 -->

							낙찰</td>
<td>2019-08-2911:00</td>
<td>
<!-- PBCT_STAT_CD IN ('0010', '0011', '0012') AND EXCT_STAT_CD != '0002' 포털 조건으로 변경-->
<a class="cm_btn_sint3" href="javascript:fn_collateralBidResultPopup('9421704','3234177','1357675');">상세이동</a>
</td>
</tr>
'''

soup = BeautifulSoup(html, "html.parser")

comments = soup.findAll(text=lambda text:isinstance(text, Comment))
for comment in comments:
   comment.extract()

dd = soup.select("dd")

print('dd :', type(dd))
print('dd 0 :', dd[0])
print('dd 1 :', dd[1].contents[0].strip())
print('dd 2 :', dd[2])
