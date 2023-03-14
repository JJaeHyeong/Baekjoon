import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []
visit = [False] * (N + 1)

def recur(num):
    if num == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
    	if visit[i] == False:
            visit[i] = True
            ans.append(i)
            recur(num + 1)
            visit[i] = False
            ans.pop()
recur(0)