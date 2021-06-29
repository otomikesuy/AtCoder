# AC
K, N = map(int, input().split())
*A, = map(int, input().split())
A = A + [K+A[0]]
chk = [0] * N
for i in range(N):
    chk[i] = A[i+1] - A[i]
chk.sort(reverse=True)
print(sum(chk[1:]))