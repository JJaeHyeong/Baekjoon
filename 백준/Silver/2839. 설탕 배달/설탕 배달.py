N = int(input())
cnt = 0

if N in [4, 7]:
    print(-1)
else:
    while N % 5 != 0:
        N -= 3
        cnt += 1
    cnt += N // 5
    print(cnt)
