N = list(str(input()))
for i in range(len(N)):
    if ord(N[i]) > 64 and ord(N[i]) < 91:
        N[i] = N[i].lower()
    else:
        N[i] = N[i].upper()
print("".join(N))