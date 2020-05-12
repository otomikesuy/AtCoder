# AC
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N, M = map(int, input().split())
if N == 1 or N == 0:
    guu = 0
else:
    guu = combinations_count(N, 2)
if M == 1 or M == 0:
    kisu = 0
else:
    kisu = combinations_count(M, 2)
print(guu + kisu)

# Model answer
N, M = map(int, input().split())
print(N*(N-1)//2 + M*(M-1)//2)