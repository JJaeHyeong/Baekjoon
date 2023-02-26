import sys
from collections import deque

n = int(input())
queue = deque()
            
tmp = deque()
for i in range(1, n + 1):
    tmp.append(i)

while len(tmp) > 1:
    tmp.popleft()
    if len(tmp) == 1:
        break
    tmp.append(tmp.popleft())
    
print(tmp[0])