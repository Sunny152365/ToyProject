# Part 1 웹 스크래핑(Web Scrapping)
#001 웹 서버에 요청하고 응답받기
import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2)

#002 웹 페이지 소스코드 확인하기(html 소스코드 출력)
import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)

#003 로봇 배제 표준(robots.txt)
"""
위키피디아(https://ko.wikipedia.org/wiki/)
case 1
    User-agent: *
    Allow: /
    설명 : 모든(*) 로봇(User-agent)에게 루트 디렉터리(/) 이하 모든 문서에 대한 접근을 허락(Allow)한다.
case 2
    User-agent: *
    Disallow: /
    설명 : 모든(*) 로봇(User-agent)에게 루트 디렉터리(/) 이하 모든 문서에 대한 접근을 차단(Disallow)한다.
case 3
    User-agent: *
    Disallow: /temp/
    설명 : 모든(*) 로봇(User-agent)에게 특정 디렉터리(/temp/)에 대한 접근을 차단(Disallow)한다.
case 4
    User-agent: googlebot
    Disallow: /
    설명 : 특정한 로봇(googlebot)에게 모든 문서에 대한 접근을 차단(Disallow)한다.
"""
import requests

urls = ["https://www.naver.com/", "https://www.pyhthon.org/"]
filename = "robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")

#004 BeautifulSoup 객체 만들기
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

print('title 태그 요소: ', soup.title)
print('title 태그 이름: ', soup.title.name)
print('title 태그 문자열: ',soup.title.string)

#005 크롬 개발자 도구
#006 웹 문서의 그림 이미지 파일을 PC에 저장하기
#007 웹 문서에 포함된 모든 하이퍼링크 추출
#008 CSS Selector 활용_1
#009 CSS Selector 활용_2
#010 구글 뉴스 클리핑_1
#011 구글 뉴스 클리핑_2
#012 동적 웹 페이지_1 다나와 자동로그인
#013 동적 웹 페이지_2 다나와 관심목록 가져오기
#014 한국은행 경제통계시스템 통계지표 활용_1
#015 한국은행 경제통계시스템 통계지표 활용_1

# Part 2 데이터 정리 및 그래프 시각화
#016