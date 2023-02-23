while True :
    s = str(input())
    rev_s = s[::-1] 
    if s == '0':
        break
    elif s == rev_s:
        print('yes')
    else:
        print('no')