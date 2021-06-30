# bubble sort1
def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(len(lis) - 1, i, -1):
            if lis[j] < lis[j-1]:
                lis[j], lis[j-1] = lis[j-1], lis[j]
    return lis

# bubble sort2
def bubble_sort_2(lis):
    for i in reversed(range(len(lis))):
        for j in range(i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

# selection sort
def selection_sort(lis):
    for i in range(0, n-1):
        minj = i
        for j in range(i, n-1):
            if a[j] < a[minj]:
                minj = j
        a[j], a[minj] = a[minj], a[j]

# Binary search (めぐる式)
def is_ok(i):
    return i <= 5

ok = -1
ng = 10
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok, ng)

# lcm
import math
def lcm(A, B):
    return int((A * B) / math.gcd(A, B))

# lcm 最小公倍数のリスト受け渡し
import math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_ret_int(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_ret_list(numbers):
    return reduce(lcm_base, numbers, 1)

# gcd 最大公約数のリスト受け渡し
import math
from functools import reduce

def gcd(x, y):
    return math.gcd(x, y)

def gcd_ret_int(*numbers):
    return reduce(math.gcd, numbers)

def gcd_ret_list(numbers):
    return reduce(math.gcd, numbers)

# least common divider 最小公約数
import math
def lcd(A, B):
    return A / math.gcd(A, B) * B


# フィボナッチ数列をDPで解く
n = 100000
F = [1, 1]
for i in range(1, n-1):
    F.append(F[i]+F[i-1])
print(F[-1])

# 累積和
# https://qiita.com/drken/items/56a6b68edef8fc605821
N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + a[i]
ans = float("-inf")
for i in range(N-K+1):
    tmp = s[K+i] - s[i]
    if ans < tmp:
        ans = tmp
print(ans)


# DFS (深さ優先探索)を再帰的に解く。
# input例
# 7 12 0 5
# 0 1
# 0 2
# 1 0
# 1 3
# 1 4
# 3 1
# 4 1
# 2 0
# 2 5
# 2 6
# 5 2
# 6 2

# DFS コーディング例
N, M, s, t = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

seen = [False for _ in range(N)]
def dfs(G, v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v] == True:
            continue
        dfs(G, next_v)

dfs(graph, s)
print(graph, seen)


# DFS 迷路
# https://atc001.contest.atcoder.jp/tasks/dfs_a
import sys
sys.setrecursionlimit(500000)
H, W = map(int, input().split())
field = [[] for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
seen = [[False for _ in range(W)] for _ in range(H)]
def dfs(h, w):
    seen[h][w] = True
    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        if nh < 0 or nw < 0 or nh >= H or nw >= W:
            continue
        if field[nh][nw] == '#':
            continue
        if seen[nh][nw]:
            continue
        dfs(nh, nw)

for h in range(H):
    field[h] = list(input())
sh, sw, gh, gw = '', '', '', ''
for h in range(H):
    for w in range(W):
        if field[h][w] == 's':
            sh, sw = h, w
        if field[h][w] == 'g':
            gh, gw = h, w
dfs(sh, sw)
if seen[gh][gw]:
    print('Yes')
else:
    print('No')

# BFS (幅優先探索)をqueueを使って解く
import queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N)
dist[0] = 0
que = queue.Queue()
que.put(0)
while not que.empty():
    v = que.get()
    for next_v in G[v]:
        if dist[next_v] != -1:
            continue
        dist[next_v] = dist[v] + 1
        que.put(next_v)
for v in range(N):
    print(v, ':', dist[v])


# 最大和問題
# Input
# 3 10
# 7 5 3
N = int(input())
*a, = map(int, input().split())
dp = [0 for _ in range(N+1)]
for i in range(N):
    dp[i+1] = max(dp[i], dp[i]+a[i])
print(dp[N])


# Knapsak問題(ナップサック)
# Input
# 4 5
# 4 2
# 5 2
# 2 1
# 8 3
N, W = map(int, input().split())
inf = float('inf')
dp = [[-inf for _ in range(W + 1)] for _ in range(N + 1)]
print(dp)
for i in range(W+1):
    dp[0][i]=0
print(dp)

for i in range(N):
    value, weight = map(int, input().split())
    for w in range(W + 1):
        if weight <= w:
            dp[i+1][w] = max(dp[i][w-weight] + value, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(dp)
print(dp[N][W])


# 部分和問題

N, A = map(int, input().split())
*a, = map(int, input().split())
# 配列の初期化
dp = [[False for _ in range(A + 1)] for _ in range(N + 1)]
dp[0][0] = True

# 0 ~ iまで
for i in range(N):
    # 0 ~ A + 1まで
    for j in range(A + 1):
        if a[i] <= j:
            dp[i+1][j] = dp[i][j-a[i]] | dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]
print(dp[N][A])



# Union Find 木のインプット例
# https://atc001.contest.atcoder.jp/tasks/unionfind_a

# Union Find 木の実装例
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        uf.union(A, B)
        continue
    if uf.find(A) == uf.find(B):
        print('Yes')
    else:
        print('No')


# ゼロ埋めsample
a = 100
b = 0.987654321
print('{0:06d}-{1:6f}'.format(a,b))


# 2次元配列のソート
w = [[1, 2], [2, 6], [3, 6], [4, 5], [5, 7]]
from operator import itemgetter
w.sort(key=itemgetter(1), reverse=True)
w.sort(key=lambda x: x[1], reverse=True)
sorted(w, key=itemgetter(1), reverse=True)


# 素数リスト
n = 100
primes = set(range(2, 2+1)) # 自然数を2~100まで作る
for i in range(2, int(n**0.5+1)): # 2~10までの繰り返しを作る
    primes.difference_update(range(i*2, n+1, i)) # 例えば2から100までの2倍、3から100までの3倍を作り消す。
primes=list(primes)

# ビット演算
a=list(product(['+','-'],repeat=3))
s=['5', '5', '3', '4']
for i in a:
    ans=s[0]+i[0]+s[1]+i[1]+s[2]+i[2]+s[3]
    if eval(ans)==7:
        print(ans+'=7')
        break

#n進数
n=64
k=-3
bi=''
while n!=0:
    bi+=str(n%abs(k))
    if k<0:n=-(-n//k)
    else:n=n//k
print(bi[::-1])


# 1 ~ 12までのmod13の逆元を一通り出すコード
# 二項係数 (nCr)
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

def modinv(a, mod):
    return modpow(a, mod -2, mod)

for i in range(1, 13):
    print(i, "'s inv: ", modinv(i, 13))


# 高速な素数判定
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

# 高速な約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


# ユークリッドの互除法でGCD
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


# 高速素因数分解
def factorize(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp % i == 0:
            cnt = 0
            while temp % i ==0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
factorize(100)


# Nまでの素数リスト
import numpy as np

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

print(seachPrimeNum(100))


