import sys
input = sys.stdin.readline

A = []
for _ in range(9):
    A.append(list(map(int,input().split())))
k = -1
n,m = 0,0
for i in range(9):
    tmp = max(A[i])
    if k < tmp :
        n = i + 1
        m = A[i].index(tmp) + 1
        k = tmp 
                
print(k)
print(n, m)