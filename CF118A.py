s = input()
for i in s:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != "y" and i != "A" and i != "E" and i != "I" and i != "O" and i != "U" and i != "Y":
        if ord(i) >= ord("a"):
            print("."+ i, end="")
        else:
            print("."+chr(ord(i)+ (ord("a") - ord("A"))), end="")