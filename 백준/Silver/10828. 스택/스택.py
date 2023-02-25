import sys
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        queue.appendleft(cmd[1])
        
    elif cmd[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif cmd[0] == 'size':
        print(len(queue))
        
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
            
    elif cmd[0] == 'top':
        if queue:
            print(queue[0])
        else:
            print(-1)