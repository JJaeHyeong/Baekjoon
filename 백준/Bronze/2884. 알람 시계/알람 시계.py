h, m = map(int,input().split())

if h == 0 and m < 45:
    h = 23
    print(h, 60 - (m-45) * -1)
elif h == 0 and m > 45:
    h = 0
    print(h, m-45)
elif h != 0 and m < 45:
    print(h-1, 60 - (m-45) * -1)
else:
    print(h, m-45)