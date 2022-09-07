#5
import time
import random

menu = []

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

while True:
    if len(menu) == 5:
        break
    else:
        a = input("메뉴 추가: ")
        if a not in menu:
            menu.append(a)
            print("현재 메뉴 수 =", len(menu))
        else:
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

x = random.choice(menu)
print("오늘의 메뉴는", menu.index(x)+1, "번째 메뉴,", x, "입니다.")



