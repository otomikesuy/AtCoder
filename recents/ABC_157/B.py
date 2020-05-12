# AC
*A1, = map(int, input().split())
*A2, = map(int, input().split())
*A3, = map(int, input().split())
A = A1 + A2 + A3
N = int(input())
a = [int(input()) for _ in range(N)]
chk = [A[:3], A[3:6], A[6:9], A[::3], A[1::3], A[2::3], A[::4], A[2:7:2]]
for c in chk:
    ans = 0
    for cc in c:
        if cc in a:
            ans += 1
    if ans == 3:
        print("Yes")
        exit()
print("No")