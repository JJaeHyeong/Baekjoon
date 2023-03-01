N = (1000 - int(input()))
coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coin:
    cnt += N // i
    N %= i
print(cnt)