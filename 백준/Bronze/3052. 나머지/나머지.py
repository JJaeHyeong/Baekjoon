from collections import Counter

tmp = [0] * 10
for i in range(10):
    tmp[i] = int(input()) % 42

dic_tmp = dict(Counter(tmp))
print(len(dic_tmp))