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
        item = input("메뉴추가 : ") #1 김치찌개 / #2 라면 / # 3 라면
        flag = 5

        # 중복확인 코드: 중복되면 flag 값을 바꿈
        for i in range(len(menu)): #1 len(menu)는0 이상 0미만, 작동 x / #2 len(menu)는0 이상 1미만, i에 0 입력 / #3 len(menu)는 0이상 2미만, i에 0,1 입력
            if menu[i] == item : #1 작동x / #2 menu[0](menu의 원소 중 0번째 것)은 아무것도 없음 -> item과 같지않음 / #3 menu[0]는 김치찌개 -> item과 같지않음, menu[1]는 라면-> item과 같음=> 계속작동
                flag = i #1 작동x / #2 작동x / #3 flag = 1이 됨
                break #1 작동x / #2 작동x / #3 멈춤(이 코드는 중복 발견되면 i에 넣을 숫자가 더 있더라도 'for i in range(len(menu))'가 더 작동하지 않게 멈추기 위함)

        # 메뉴추가 코드: 입력값(item)이, 중복이면 원래것 삭제 후 새것 추가/ 중복아니면 걍 추가
        if flag != 5: #1 flag = 5(15번째줄 유지) -> else로 / #2 flag = 5(15번째줄 유지) -> else로 / #3 flag = 1로 바꼈으므로 'flag != 5' 로 작동
            print("이미 있는 메뉴에요! 다른 메뉴를 입력해주세요.") #1 작동x / #2 작동x / #3 print 작동
            del menu[i] #1 작동x / #2 작동x / #3 flag = i = 1 이니까 del menu[1] 작동해서 menu = ['김치찌개', '라면']에서 1번째 값인 '라면' 제거(중복된 것 중 기존에 있던 것 제거)) 그래서 menu = ['김치찌개]가 됨
            menu.append(item) #1 작동x / #2 작동x / #3 menu = ['김치찌개]에 #3때 입력한 item '라면'을 추가해서 menu = ['김치찌개', '라면']가 됨 => 결과적으로 중복되면, 기존 거 지우고 새로운 거 추가
        else:
            menu.append(item)  #1 menu에 입력값(item) '김치찌개' 추가 -> menu = ['김치찌개'] / #2 menu에 입력값(item) '라면' 추가 -> menu = ['김치찌개', '라면'] / #3 작동x
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
print("오늘의 메뉴는", menu.index(random.choice(menu))+1, "번째 메뉴,", random.choice(menu), "입니다.")