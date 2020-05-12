# AC
N, R = map(int, input().split())
if N >= 10:
    print(R)
    exit()
else:
    print(100 * (10 - N) + R)