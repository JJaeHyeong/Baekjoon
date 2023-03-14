n = []
for _ in range(28):
    n.append(int(input()))
check_list = range(1, 31)

for i in check_list:
    if i not in n:
        print(i)