# AC
A, B, C, K = map(int, input().split())
ans = 0

if K >= A:
    ans += A
    K -= A
else:
    ans += K
    K = 0

if K >= B:
    K -= B
else:
    K = 0

if K >= C:
    ans -= C
else:
    ans -= K
    K = 0
print(ans)
