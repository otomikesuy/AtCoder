# AC
N = int(input())
X = sorted(list(map(int, input().split())))
p = [[] for _ in range(max(X))]
for i in range(max(X)):
    for j in X:
        p[i].append((j - (i+1)) ** 2)
sums = [sum(pp) for pp in p]
print(min(sums))