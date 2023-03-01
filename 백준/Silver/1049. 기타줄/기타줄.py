N, M = map(int, input().split())

pack = []
sin = []
for i in range(M):
    p, s = map(int, input().split())
    pack.append(p)
    sin.append(s)

min_pack = min(pack)
min_sin = min(sin)

if min_pack <= 6 * min_sin:
    ans = (N // 6) * min_pack
    if N % 6 != 0:
        ans += min_pack if min_pack < (N % 6) * min_sin else (N % 6) * min_sin
else:
    ans = N * min_sin

print(ans)