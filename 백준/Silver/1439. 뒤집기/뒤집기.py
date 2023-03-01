S = input()
A = list(filter(None, S.split(sep='0')))
B = list(filter(None, S.split(sep='1')))

print(min(len(A), len(B)))