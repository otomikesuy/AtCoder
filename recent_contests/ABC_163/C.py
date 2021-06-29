# AC (review)
N = int(input())
*A, = map(int, input().split())
dic = {i: 0 for i in range(1, N+1)}
for x in A:
    if x in dic:
        dic[x] += 1
for k, v in dic.items():
    print(v)