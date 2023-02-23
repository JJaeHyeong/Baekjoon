def factorial(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
    return tmp

N, K = map(int, input().split())
print(int((factorial(N)) / ((factorial(K) * factorial(N - K)))))