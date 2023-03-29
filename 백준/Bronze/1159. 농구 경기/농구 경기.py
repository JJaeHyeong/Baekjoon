N = int(input())
tmp = []
for _ in range(N):
    name = list(input())
    a = name[0]
    tmp += a
undupli = set(tmp)
result = []
for i in undupli:
    if tmp.count(i) >= 5:
        result.append(i)
if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print('PREDAJA')