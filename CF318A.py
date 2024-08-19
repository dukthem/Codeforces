nk = list(map(int, input().split()))
arr_odd = []
arr_even = []
for i in range(nk[0]-1, -1, -1):
    if (nk[0]-i) % 2 != 0:
        arr_odd.append(nk[0]-i)
    else:
        arr_even.append(nk[0]-i)
    
arr_sum = arr_odd + arr_even
print(arr_sum[nk[1]-1])