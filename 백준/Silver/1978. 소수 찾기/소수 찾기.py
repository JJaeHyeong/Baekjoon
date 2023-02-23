def prime(n):
    if n < 2:
        return False    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cnt = 0
N = int(input())
tmp = input().split()

for i in range(N):
    if prime(int(tmp[i])) == True:
        cnt += 1
        
print(cnt)