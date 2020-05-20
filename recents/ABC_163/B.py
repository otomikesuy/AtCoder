# AC (review)
N, M = map(int, input().split())
*A, = map(int, input().split())
ttl = sum(A)
if ttl > N:
    print(-1)
else:
    print(N-ttl)