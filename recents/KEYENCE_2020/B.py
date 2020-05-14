# AC after contest
N = int(input())
A = []
for i in range(N):
    x, l = map(int, input().split())
    A.append([x+l, x-l])
A.sort()
ans = 1
check1 = A[0]
for i in range(1, N):
    check2 = A[i]
    if check1[0] <= check2[1]:
        ans += 1
        check1 = check2
print(ans)