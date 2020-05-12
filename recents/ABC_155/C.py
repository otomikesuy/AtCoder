# AC
from collections import Counter
N = int(input())
S = Counter([input() for _ in range(N)])
v = max(S.values())
s = sorted(S.most_common())
if len(S) == 1:
    print(list(S)[0])
    exit()
for k, val in s:
    if val == v:
        print(k)

# Model answer
from collections import Counter
N = int(input())
S = Counter(input() for _ in range(N))
ma = max(S.values())
for v in sorted(k for k, v in S.items() if v == ma):
    print(v)