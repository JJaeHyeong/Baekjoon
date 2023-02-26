n = int(input())

room = 1
cnt = 1
while room < n:
    room += (6 * cnt)
    cnt += 1

print(cnt)
