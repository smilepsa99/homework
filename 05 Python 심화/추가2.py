text = input("Enter a sentence : ")

l_text = text.lower()
a = l_text.count("a")
e = l_text.count("e")
i = l_text.count("i")
o = l_text.count("o")
u = l_text.count("u")

result = a+e+i+o+u

if result == 1:
    print("Your sentence contains", result, "vowel.")
else:
    print("Your sentence contains", result, "vowels.")