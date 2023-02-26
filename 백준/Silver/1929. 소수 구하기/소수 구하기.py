M, N =map(int,input().split())

prime = [True] * (N + 1)
prime[1] = False

for i in range(2, N + 1):
    for j in range(2, N + 1):
        if i * j > N:
            break
        prime[i * j] = False

for i in range(M, N + 1):
    if prime[i]:
        print(i)