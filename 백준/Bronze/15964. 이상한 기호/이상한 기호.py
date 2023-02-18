def temp(A, B):
    return (A + B) * (A - B)

A, B = map(int, input().split())
print(temp(A, B))