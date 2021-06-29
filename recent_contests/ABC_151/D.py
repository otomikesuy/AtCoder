# AC with guide (review)
import queue
H, W = map(int, input().split())
g = [list(input()) for _ in range(H)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(g, sh, sw):
    dist = [[-1] * W for _ in range(H)]
    que = queue.Queue()
    res = 0
    que.put((sh,sw))
    dist[sh][sw] = 0
    while not que.empty():
        sh, sw = que.get()
        res = max(res, dist[sh][sw])
        for i in range(4):
            nh = sh + dx[i]
            nw = sw + dy[i]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if g[nh][nw] == '#':
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[sh][sw] + 1
                que.put((nh, nw))
    return res

ans = 0
for sh in range(H):
    for sw in range(W):
        if g[sh][sw] == '#':
            continue
        ans = max(ans, bfs(g, sh, sw))
print(ans)