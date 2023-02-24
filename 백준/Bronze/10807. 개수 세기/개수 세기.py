N = int(input())
tmp = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if tmp[i] == v:
        cnt += 1
print(cnt)