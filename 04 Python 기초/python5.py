#5
import time
import random

menu = []

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

while True:
    if len(menu) == 5 :
        break
    else:
        item = input("메뉴추가 : ")
        #!!!!!!!!!!!!!!!!!!!!!!!!이해안됨(17~29)!!!!!!!!!!!!!!!!!!!!!!!!
        flag = 5

        for i in range(len(menu)):
            if menu[i] == item :
                flag = i
                break

        if flag != 5:
            print("이미 있는 메뉴에요! 다른 메뉴를 입력해주세요.")
            del menu[i]
            menu.append(item)
        else:
            menu.append(item)
        #!!!!!!!!!!!!!!!!!!!!!!!!이해안됨(17~29)!!!!!!!!!!!!!!!!!!!!!!!!
        print("현재 메뉴 수 = ", len(menu))

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

print()
print("오늘의 메뉴는", menu.index(random.choice(menu)), "번째 메뉴,", random.choice(menu), "입니다.")