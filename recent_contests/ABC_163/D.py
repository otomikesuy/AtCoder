# AC with guide (review)
N, K = map(int, input().split())
ans = 0
MOD = 10 ** 9 + 7
for k in range(K, N + 2):
    mini = k * (k - 1) // 2
    maxi = k * (2 * N - k + 1) // 2
    add = maxi - mini + 1
    ans = (ans + add) % MOD
print(ans)