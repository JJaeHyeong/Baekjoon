import math

S = int(input())

X = int(math.sqrt(2 * S))
while True:
    N = X * (X + 1) // 2
    if N <= S:
        break
    X -= 1

print(X)
