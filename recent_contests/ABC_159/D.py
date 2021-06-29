# AC after contest
from collections import Counter
N = int(input())
*A, = map(int, input().split())
cnt = Counter(A)
ttl = 0
for v in cnt.values():
    ttl += v*(v-1)//2
for a in A:
    print(ttl - (cnt[a] - 1))

# Model answer
def choose2(n):
    return n*(n-1) // 2
from collections import Counter
N = int(input())
*A, = map(int, input().split())
cnt = Counter(A)
ttl = 0
for v in cnt.values():
    ttl += choose2(v)
for a in A:
    ans = ttl
    ans -= choose2(cnt[a])
    ans += choose2(cnt[a] - 1)
    print(ans)
    cnt[a] + 1