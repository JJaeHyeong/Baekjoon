N, X = map(int, input().split())
A = input().split()
ans = []
for i in range(N):
    A[i] = int(A[i])
    
for num in A:
    if num < X:
        ans.append(num)
        
print(' '.join(map(str, ans)))