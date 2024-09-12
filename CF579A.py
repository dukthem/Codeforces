def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num), 'b')
    return binary_str
n = int(input())
d = decimal_to_binary(n)
a = str(d)
cnt = 0
for i in range(len(a)):
    if a[i] == "1":
        cnt += 1
print(cnt)
# x = int(input())
# if x % 2 == 0:
#     print(1)
# else:
#     # print(2)
    