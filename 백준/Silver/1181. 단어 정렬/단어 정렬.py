n = int(input())
a = []
for i in range(n):
    word = input().strip()
    a.append(word)
unq = list(set(a))
unq.sort(key=lambda x: (len(x), x))
for word in unq:
    print(word)