N = int(input())
p = list(map(int, input().split()))
p.sort()
a = 0
for i in range(N):
    a += sum(p[:(i+1)])
    
print(a)