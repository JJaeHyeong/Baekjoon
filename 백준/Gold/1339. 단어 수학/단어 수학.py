from collections import defaultdict
N = int(input())
words = []
weight = defaultdict(int)
dicts = {}
ans = 0

for _ in range(N):
    w = list(input().rstrip())
    words.append(w)
    for i in range(len(w)-1, -1, -1):
        weight[w[i]] += 10 ** (len(w) - i)

sorted_weight = sorted(weight.items(), key=lambda x : x[1], reverse=True)

tmp = 9
for i, j in sorted_weight:
    dicts[i] = str(tmp)
    tmp -= 1

for word in words:
    num = ''
    for j in word:
        num += dicts[j]
    ans += int(num)

print(ans)