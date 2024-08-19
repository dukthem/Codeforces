knw = list(map(int, input().split()))
req_sum = ((knw[2]*knw[0])*(knw[2]+1))//2
print(max(req_sum - knw[1], 0))