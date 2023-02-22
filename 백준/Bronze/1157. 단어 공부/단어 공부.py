a = str(input())
s = a.upper()
dic = {}
for chr in s:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

max_value = max(dic.values())
max_keys = [k for k, v in dic.items() if v == max_value]

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])