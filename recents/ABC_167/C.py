# AC after contest
from itertools import combinations
N, M, X = map(int, input().split())
books = []
for _ in range(N):
    books.append(list(map(int, input().split())))
P = []
for i in range(1, N+1):
    for item in list(combinations(books, i)):
        P.append(item)
ans = 10 ** 9 + 1
for items in P:
    price = 0
    chk = [0] * M
    for p in items:
        price += p[0]
        for i, item in enumerate(p[1:]):
            chk[i] += item
        if all(c >= X for c in chk):
            ans = min(ans, price)
            break
if ans == 10 ** 9 + 1:
    ans = -1
print(ans)
