import sys
input = sys.stdin.readline

## 0 = white / 1 = black
board = [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         ]

check = []
for i in range(8):
    check.append(list(input().strip()))
    
ans = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 0 and check[i][j] == 'F':
            ans += 1
            
print(ans)
