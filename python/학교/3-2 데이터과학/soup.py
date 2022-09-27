from bs4 import BeautifulSoup

html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul\class="menu"><li><a href=http://www.hanbit.co.kr/member/login.html \class="login">로그인 </a></li></ul><ul class="brand"><li><a href="http://www.\hanbit.co.kr/media/>한빛미디어<li><a href="http://www.hanbit.co.kr/\academy/">한빛아카데미</a></li></ul></div>'


soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

soup.h1
