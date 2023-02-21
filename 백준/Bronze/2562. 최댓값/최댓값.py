temp = []
for i in range(1, 10):
    N = int(input())
    temp.append(N)
    
ans = max(temp)
print(ans)
print((temp.index(ans) + 1))