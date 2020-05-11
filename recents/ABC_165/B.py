# AC
X = int(input())
K = 100
for i in range(1, 10000000000):
    K = int(K * 1.01)
    if K >= X:
        print(i)
        exit()