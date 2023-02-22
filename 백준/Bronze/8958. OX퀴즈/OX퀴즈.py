# TC 개수 입력
t = int(input())

for i in range(t):
    s = input()   # 문자열 입력
    cnt = 0
    ans = 0

    for c in s:
        if c == 'O':   # 연속된 O의 개수를 1 증가
            cnt += 1   # 현재 문자까지의 점수를 계산하여 총합에 더함
            ans += cnt
        else:
            cnt = 0   # 연속된 O의 개수 초기화
    print(ans)