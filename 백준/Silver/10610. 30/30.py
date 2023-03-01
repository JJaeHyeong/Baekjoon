N = str(input())
num_list = list(map(int, str(N)))
num_list.sort(reverse=True)

N = "".join([str(_) for _ in num_list])

if int(N) % 30 == 0:
    print(N)
else:
    print(-1)