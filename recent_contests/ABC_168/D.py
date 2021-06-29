# AC after contest
from queue import Queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
que = Queue()
que.put(0)
visit = [0] * N
ans = [0] * N
while not que.empty():
    v = que.get()
    for next_v in G[v]:
        if visit[next_v] == 1:
            continue
        ans[next_v] = v
        visit[next_v] = 1
        que.put(next_v)
print("Yes")
print(*list(map(lambda x: x+1, ans[1:])), sep='\n')