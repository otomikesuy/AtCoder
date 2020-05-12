# AC
import math
A, B = map(int, input().split())
eight = 0.08
ten = 0.1
for i in range(100*11):
    if math.floor(i * eight) == A and math.floor(i * ten) == B:
        print(i)
        exit()
print(-1)