A, B, C = map(int,input().split())

max = A
if B > max :
    max = B
if C > max : 
    max = C

if A == B == C:
  print(10000+A*1000)
elif A==B or A==C :
  print(1000+A*100)
elif B==C:
  print(1000+B*100)
else :
  print(100 * max)