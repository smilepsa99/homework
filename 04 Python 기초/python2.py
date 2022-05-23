#2
a = {}

a["이름"] = "박상아"
a["나이"] = "24살"
a["학번"] = "20184933"
a["학과"] = "예술경영"
a["생일"] = "7월9일"
print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]
print(a)
print(len(a))
print()

a = dict(이름 = "박상아", 나이 = "24살", 학번 = "20184933", 학과 = "예술경영", 생일 = "7월9일")
a.clear()
print(a)
print(len(a))