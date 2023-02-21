N = int(input())
tmp = list(str(input()))
ans = 0

for i in range(N):
    ans = ans + int(tmp[i])
    
print(ans)