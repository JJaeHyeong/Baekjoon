N = int(input())
tmp = []
ans = []
for _ in range(N):
    tmp.append(int(input()))
tmp.sort()

for i in range(0, N, 1):
    ans.append(tmp[i] * (N - i))
ans.sort()
print(ans[-1])