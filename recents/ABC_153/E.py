# AC after contest
import sys
input = sys.stdin.readline
H, N = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
dp = [[float("inf") for j in range(H+1)] for i in range(N+1)]
for i in range(N):
    for j in range(H+1):
        if j <= A[i]:
            dp[i+1][j] = min(dp[i][j], B[i])
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-A[i]] + B[i])
print(dp[N][H])