# AC after contest
N, X, Y = map(int, input().split())
X -= 1
Y -= 1
ans = [0] * N
for i in range(N):
    for j in range(i+1,N):
        d1 = j - i
        d2 = abs(X-i) + abs(Y-j) + 1
        ans[min(d1, d2)] += 1
print(*ans[1:], sep='\n')