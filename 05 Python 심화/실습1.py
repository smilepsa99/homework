n = int(input("자연수를 입력해주세요 : "))
mysum = n*(n+1)/2
result = int(mysum)
print("1 부터", n, "까지의 합은", result, "입니다.")

# !def를 사용할 경우!
# def mysum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     return sum

# n = int(input("자연수를 입력해주세요 : "))
# result = mysum(n)
# print("1 부터", n, "까지의 합은", result, "입니다.")
