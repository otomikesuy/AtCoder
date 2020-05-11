# AC
def cal(x):
    import math
    return math.floor(A*x/B)
A, B, N = map(int, input().split())
if N < B:
    x = N
else:
    x = B - 1
print(cal(x))