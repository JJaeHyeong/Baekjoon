def floor(k, n):
    tmp = [[0]*(n+1) for _ in range(k+1)]
    tmp[0][1] = 1
    for i in range(1, n+1):
        tmp[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            tmp[i][j] = sum(tmp[i-1][1:j+1])
    return tmp[k][n]

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(floor(k,n))
