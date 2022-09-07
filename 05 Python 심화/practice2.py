from winreg import KEY_READ
import requests
import json

cityname = "Seoul"
apikey = "7a8365084cc7fe27518d117747ec4001"
lang = "kr"
units = "metric"

weather = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}&lang={lang}&units={units}"
response = requests.get(weather)
result = json.loads(response.text)

#print(result)
print(result["name"],"의 날씨입니다.")
print("날씨는",result["weather"][0]["description"],"입니다.")
print("현재 온도는",result["main"]["temp"],"입니다.")
print("체감 온도는",result["main"]["feels_like"],"입니다.")
print("최저 기온은",result["main"]["temp_min"],"입니다.")
print("최고 기온은",result["main"]["temp_max"],"입니다.")
print("습도는",result["main"]["humidity"],"입니다.")
print("기압은",result["main"]["pressure"],"입니다.")
print("풍향은",result["wind"]["deg"],"입니다.")
print("풍속은",result["wind"]["speed"],"입니다.")
