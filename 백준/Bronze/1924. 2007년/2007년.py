import sys
input = sys.stdin.readline

x, y = map(int, input().split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = sum(months[:x-1]) + (y - 1)
ans = days[(total_days) % 7]
print(ans)
