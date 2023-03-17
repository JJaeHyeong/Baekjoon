import sys
input = sys.stdin.readline

n = int(input())
pp = [list(map(int, input().split())) for _ in range(n)]

temp = []
for i in range(n):
    cnt = 1
    
    for j in range(n):
        if (pp[i][0] < pp[j][0]) and (pp[i][1] < pp[j][1]):
            cnt += 1
        else:
            pass
    temp.append(cnt)   

for t in temp:
    print(t, end=' ')