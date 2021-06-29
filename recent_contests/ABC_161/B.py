# AC
N, M = map(int, input().split())
*a, = map(int, input().split())
a.sort(reverse=True)
if a[M-1] >= (sum(a) / (4*M)):
    print('Yes')
else:
    print('No')