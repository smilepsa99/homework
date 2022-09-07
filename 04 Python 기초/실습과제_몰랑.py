n = int(input("자연수를 입력하세요 : "))

#1
for i in range(n):
    x = "*" * (i+1)
    print(x)

#2
for i in range(n):
    x = " " * (n-(i+1)) + "*" * (i+1)
    print(x)

#3
for i in range(n):
    x = " " * (n-(i+1)) + "*" * (2*i+1)
    print(x)

#4
for i in range(n):
    x = " " * i + "*" * (-2*i+2*n-1)
    print(x)

#복습#################################################################################################################

n = int(input("자연수를 입력해주세요 : "))

#1
for i in range(n):      # 어떤 숫자범위 안에서 하나씩 숫자를 뽑을 때 'range()'로 써야 함 주의!(걍 숫자만 달랑 쓰면 안됨)
                        # range(n) 은 range(0,n)을 뜻하며, 즉 "0아성 n미만"을 말함
    answer = "*"*(i+1)
    print(answer)

#2
for i in range(n):
    answer = " "*(n-(i+1)) + "*"*(i+1)
    print(answer)

#3
for i in range(n):
    answer = " "*(n-(i+1)) + "*"*(2*i+1)
    print(answer)

#4
for i in range(n):
    answer = " "*i + "*"*(2*n-1-2*i)
    print(answer)
