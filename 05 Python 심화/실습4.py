list = []

while True:
    n = input("숫자를 입력해주세요 : ")
    if n == "q":
        print(len(list), "개의 숫자 중 최솟값은",list.index(min(list))+1, "번째 수", min(list), "입니다.")
        print(len(list), "개의 숫자 중 최댓값은",list.index(max(list))+1, "번째 수", max(list), "입니다.")
        break
    else:
        list.append(int(n))