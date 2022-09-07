#날씨정보 받아오기

import requests
import json

apikey = "7a8365084cc7fe27518d117747ec4001"
lang = "kr"
units = "metric"
api = f"https://api.openweathermap.org/data/2.5/weather?lat=38&lon=147&appid={apikey}&lang={lang}&units={units}"

result = requests.get(api)
data = json.loads(result.text)

print(result.text)
print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
print("현재 온도는",data["main"]["temp"], "입니다.")
print("체감 온도는",data["main"]["feels_like"], "입니다.")
print("최저 기온은",data["main"]["temp_min"], "입니다.")
print("최고 기온은",data["main"]["temp_max"], "입니다.")
print("현재 습도는",data["main"]["humidity"], "입니다.")
print("현재 기압은",data["main"]["pressure"], "입니다.")
print("현재 풍향은",data["wind"]["deg"], "입니다.")
print("현재 풍속은",data["wind"]["speed"], "입니다.")