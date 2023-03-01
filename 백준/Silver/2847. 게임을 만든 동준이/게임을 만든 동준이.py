N = int(input())
arr = []
cnt = 0
for _ in range(N):
    score=int(input())
    arr.append(score)

for i in range(N - 1):
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            cnt += 1
            arr[i] = arr[i + 1] - 1

        if arr[i] > arr[i + 1]:
            cnt += arr[i] - arr[i + 1] + 1
            arr[i] = arr[i + 1] - 1
print(cnt)