from collections import deque

n, m, k, x = map(int, input().split())

# 각 도시에 연결된 도시 정보를 저장하는 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 정보를 저장하는 리스트
distance = [-1] * (n + 1)
distance[x] = 0

# BFS 알고리즘 적용
q = deque([x])
while q:
    now = q.popleft()
    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            q.append(next_city)

# 거리가 K인 도시 번호를 저장하는 리스트
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

# 출력
if not result:
    print(-1)
else:
    result.sort()
    for city in result:
        print(city)