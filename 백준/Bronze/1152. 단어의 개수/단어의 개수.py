a = input()
b = a.strip()
if a == ' ':
    print('0')
else:
    print(b.count(' ') + 1)