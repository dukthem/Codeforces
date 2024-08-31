n = int(input())
sum = 0
for i in range(n):
    shape = input()
    if shape == "Icosahedron":
        sum += 20
    elif shape == "Dodecahedron":
        sum += 12
    elif shape == "Octahedron":
        sum += 8
    elif shape == "Cube":
        sum += 6
    else:
        sum += 4
print(sum)