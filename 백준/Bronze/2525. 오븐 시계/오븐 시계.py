A, B = map(int, input().split())
C = int(input())

if 60 <= C <= 1000:
    time = C // 60
    minute = C % 60
    A += time
    B += minute
    
    if B >= 60:
        A += 1
        B -= 60
    if A >= 24:
        A -= 24

else:
    if B + C >= 60:
        A += 1
        B = B + C - 60
    else:
        B += C
    if A >= 24:
        A -= 24
print(A, B)