s = input()
arr = s.split("+")
arr.sort()
for i in range(0, len(arr)):
    print(arr[i], end="")
    if i != len(arr)-1:
        print('+', end="")
    