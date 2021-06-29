# AC
N, M = map(int, input().split())
*H, = map(int, input().split())
set_list = [[] for _ in range(N)]
import sys
input = sys.stdin.readline
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    A -= 1
    B -= 1
    set_list[A].append(B)
    set_list[B].append(A)
ans = 0
for i in range(N):
    chk = True
    for j in set_list[i]:
        if H[i] > H[j]:
            continue
        else:
            chk = False
    if chk:
        ans += 1
print(ans)