# AC (review)
import itertools
n = int(input())
a = tuple(i for i in range(1, n+1))
x = tuple(map(int, input().split()))
y = tuple(map(int, input().split()))

for i, z in enumerate(tuple(itertools.permutations(a))):
    if z == x:
        x_count = i
    if z == y:
        y_count = i
print(abs(x_count - y_count))