n = int(input())
exist = n
cycle = 0

while True:
    cycle += 1
    new_num = int(str(n % 10) + str((n // 10 + n % 10) % 10))
    if new_num == exist:
        break
    n = new_num

print(cycle)