#4
total_dictionary = {}

while True:
    a = input("Enter a fruit type (q to quit): ")
    if a == "q":
        break
    else:
        b = input("Enter the weight in kg : ")
        total_dictionary[a] = b

print(total_dictionary)