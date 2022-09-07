string = input("단어를 입력해주세요 : ")
lower_string = string.lower()

a = lower_string.count("a")
e = lower_string.count("e")
i = lower_string.count("i")
o = lower_string.count("o")
u = lower_string.count("u")

print("a는", a, "개 포함되어 있습니다.")
print("e는", e, "개 포함되어 있습니다.")
print("i는", i, "개 포함되어 있습니다.")
print("o는", o, "개 포함되어 있습니다.")
print("u는", u, "개 포함되어 있습니다.")
