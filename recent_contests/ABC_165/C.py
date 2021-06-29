# AC
from itertools import combinations_with_replacement
N, M, Q = map(int, input().split())
chk = []
for _ in range(Q):
    *abcd, = map(int, input().split())
    chk.append(abcd)

li = [list(x) for x in list(combinations_with_replacement(range(1, M+1), N))]
ans = 0
for item in li:
    sub = 0
    for c in chk:
        if item[c[1]-1] - item[c[0]-1] == c[2]:
            sub += c[3]
    ans = max(ans, sub)
print(ans)