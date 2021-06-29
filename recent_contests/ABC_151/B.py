# AC (review)
N, K, M = map(int, input().split())
*A, = map(int, input().split())

for i in range(K + 1):
    avg = (sum(A) + i) / (len(A) + 1)
    if avg >= M:
        print(i)
        exit()
print(-1)