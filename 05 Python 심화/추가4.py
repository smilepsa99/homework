list = []

while True:
    n = int(input("Enter a number: "))
    if n < 0:
        break
    else:
        list.append(n)

x = max(list)
print("The largest number entered was", x)