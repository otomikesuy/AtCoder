# AC after contest
import sys
sys.setrecursionlimit(1000000)
K = int(input())
all = []
def dfs(number):
    all.append(number)
    if len(str(number)) == 10:
        return
    for i in range(-1, 2):
        n_number = number % 10 + i
        if n_number >= 0 and n_number <= 9:
            dfs(number*10+n_number)

for i in range(1, 10):
    dfs(i)
all.sort()
print(all[K-1])