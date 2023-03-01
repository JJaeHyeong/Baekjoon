board = input().strip()
N = len(board)

count_x = 0
count_cont_x = 0
result = ""

odd_x_count = 0
for i in range(N):
    if board[i] == "X":
        count_x += 1
        count_cont_x += 1
        if count_cont_x == 4:
            result += "AAAA"
            count_cont_x = 0
    else:
        if count_cont_x % 4 != 0:
            result += "AAAA" * (count_cont_x // 4)
            if count_cont_x % 4 == 2:
                result += "BB"
            count_cont_x = 0
        if count_x % 2 != 0:
            odd_x_count += 1
            if odd_x_count > 1:
                print(-1)
                exit()
        count_x = 0
        result += "."

if count_cont_x % 4 != 0:
    result += "AAAA" * (count_cont_x // 4)
    if count_cont_x % 4 == 2:
        result += "BB"
if count_x % 2 != 0:
    odd_x_count += 1
    if odd_x_count > 1:
        print(-1)
        exit()

if odd_x_count == 1:
    print(-1)
elif "X" in result:
    print(-1)
else:
    print(result)
