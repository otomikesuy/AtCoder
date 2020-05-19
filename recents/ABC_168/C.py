# AC after contest
import math
A, B, H, M = map(int, input().split())
cho = 6 * M
tan = 30 * H
gap = 0.5 * M
kakudo = tan + gap - cho
if kakudo == 180:
    print(A+B)
    exit()
if kakudo > 180:
    kakudo = 360 - kakudo
ans = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(kakudo))
print(ans ** 0.5)