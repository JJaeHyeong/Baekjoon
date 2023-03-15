def d(n):
    return n + sum(map(int, str(n)))

numbers = set(range(1, 10001))

for i in range(1, 10001):
    self_num = d(i)
    if self_num <= 10000:
        numbers.discard(self_num)

for num in sorted(numbers):
    print(num)