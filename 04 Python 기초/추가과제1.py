import time

n1 = int(input("자연수 나눗셈을 진행합니다. 숫자를 입력하세요 : "))
n2 = int(input("어떤 숫자로 나눌지 입력하세요 : "))

print("몫과 나머지를 계산중입니다.")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print( n1,"÷", n2, "의 몫은", int(n1/n2), ", 나머지는", int(n1%n2), "입니다.")