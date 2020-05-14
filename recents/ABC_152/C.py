# AC after contest
N = int(input())
P = list(map(int, input().split()))
curMin = float("inf")
ans = 0
for x in P:
    curMin = min(curMin, x)
    if curMin == x:
        ans += 1
print(ans)