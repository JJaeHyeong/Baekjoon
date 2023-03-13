import sys
N = int(input())
for x in range(N):
   a, b = map(int, sys.stdin.readline().split())
   print(a + b)