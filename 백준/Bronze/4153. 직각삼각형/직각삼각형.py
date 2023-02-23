while True:
    a, b, c = map(int, input().split())
    absq = a ** 2 + b ** 2
    acsq = a ** 2 + c ** 2
    bcsq = b ** 2 + c ** 2
    
    if a == 0 & b == 0 & c == 0:
        break
    elif absq == c ** 2 or acsq == b ** 2 or bcsq == a ** 2:
        print('right')
    else:
        print('wrong')