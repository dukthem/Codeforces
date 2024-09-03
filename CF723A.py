xyz = list(map(int, input().split()))
xyz.sort()
print((xyz[1]-xyz[0]) + (xyz[2] - xyz[1]))