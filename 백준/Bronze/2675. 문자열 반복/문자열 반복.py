T = int(input())
for i in range(T):
    R, S = input().split()
    temp = list(S)
    for j in range(len(temp)):
        print(temp[j] * int(R), end='')
    print()