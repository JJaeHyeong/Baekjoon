while True:
    cnt = 0
    tmp = input()
    if tmp == '#':
        break
    for i in tmp:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1
            
    print(cnt)