# AC
N, K = map(int, input().split())
darega = [[] for _ in range(N)]
for i in range(K):
    _ = input()
    hito = map(int, input().split())
    for j in hito:
        darega[j-1].append(i+1)
ans = 0
for x in darega:
    if x == []:
        ans += 1
print(ans)