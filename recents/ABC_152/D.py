# AC after contest
N = int(input())
cnt = [[0] * 10 for _ in range(10)]
for i in range(1, N+1):
    i = str(i)
    l = int(i[0])
    r = int(i[-1])
    cnt[l][r] += 1
ans = 0
for l in range(10):
    for r in range(10):
        ans += cnt[l][r] * cnt[r][l]
print(ans)