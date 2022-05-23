#5
import time
import random

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

list = [] #중복o 입력값들
menu = [] #중복x 입력값들

while True:
    if len(menu) == 5 :
        break
    else:
        food = input("메뉴추가 : ")
        list.append(food)
        for x in list:
            if x not in menu:
                menu.append(x)
                print("현재 메뉴 수 = ", len(menu))
            elif x in menu:
                print("이미 있는 메뉴에요! 다른 메뉴를 입력해주세요.")

print()
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print()
print(menu)
print("과연 오늘의 메뉴는?")

print()
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print("오늘의 메뉴는", menu.index(random.choice(menu)), "번째 메뉴,", random.choice(menu), "입니다.")