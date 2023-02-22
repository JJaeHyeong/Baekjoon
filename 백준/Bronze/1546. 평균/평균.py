n = int(input())
score = input().split()
sum = 0

for i in range(n):
    score[i] = int(score[i])   # 정수형태로 score 리스트에 재입력
    
for i in score:
    i = (i / max(score)) * 100   # 점수/M*100 ==> 문제 조건 공식
    sum += i
print(sum / n)