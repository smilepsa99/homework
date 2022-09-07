import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

#file = open("bugs.html","w",encoding="utf-8")
#file.write(response.text)
#file.close()
# -> 실시간 차트 제목이 어떤 코드에 있는지 확인하기 위함 

results = soup.findAll("p","title")
    
file2 = open("practice1.txt","w",encoding="utf-8")
file2.write(str(datetime.now())+"의 벅스 실시간 차트 순위입니다.\n") # str() → 숫자를 문자열 형태로 바꿔주는 함수
rank = 1
for x in results:
    file2.write(str(rank)+"위 : "+x.get_text()+"\n")
    rank = rank + 1 #축약하면 rank += 1
file2.close()



