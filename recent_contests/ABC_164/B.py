# AC
A, B, C, D = map(int, input().split())
for _ in range(1000):
    C = C - B
    A = A - D
    if C <= 0:
        print("Yes")
        exit()
    if A <= 0:
        print("No")
        exit()