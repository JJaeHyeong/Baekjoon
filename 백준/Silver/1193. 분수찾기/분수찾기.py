import sys
input = sys.stdin.readline

X = int(input())

cnt = 0
tmp = 0
while cnt < X:
    tmp += 1
    cnt += tmp

if tmp % 2 == 0:
    bunja = X - (cnt - tmp)
    bunmo = tmp - bunja + 1
else:
    bunmo = X - (cnt - tmp)
    bunja = tmp - bunmo + 1

print(f"{bunja}/{bunmo}")