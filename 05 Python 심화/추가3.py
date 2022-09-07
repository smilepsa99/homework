name_list = []
y = 0

while True:
    name = input("Enter a name (q to quit): ")
    if name == "q":
        break
    else:
        split_name = name.split()
        name_list.extend(split_name)
        x = len(name_list)

        l_name = name.lower()
        count = l_name.count("a")
        y = y + count

print("Numbers of names and letter 'a' :", x,",", y)
