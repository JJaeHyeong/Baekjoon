N = int(input())
tmp = []
for i in range(N):
    tmp.append(int(input()))
tmp.sort()
for j in range(N):
    print(tmp[j])