# AC
H = int(input())
W = int(input())
N = int(input())
for i in range(1000000):
    if max(H, W) * i >= N:
        print(i)
        exit()