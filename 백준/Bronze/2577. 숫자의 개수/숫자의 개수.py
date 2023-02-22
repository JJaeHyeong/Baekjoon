A = int(input())
B = int(input())
C = int(input())
tmp = list(str(A * B * C))
tmp.sort()
cnt = {}
for n in tmp:
    if n not in cnt:
        cnt[n] = 1
    else:
        cnt[n] += 1

for i in range(0, 10):
    print(cnt.get(str(i), 0))