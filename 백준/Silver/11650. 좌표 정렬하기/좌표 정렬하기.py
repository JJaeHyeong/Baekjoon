n = int(input())

tmp = []
for _ in range(n):
    x, y = map(int, input().split())
    tmp.append((x, y))

tmp = sorted(tmp)

for point in tmp:
    print(point[0], point[1])