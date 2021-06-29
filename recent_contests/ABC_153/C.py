# AC
N, K = map(int, input().split())
H = sorted(list(map(int, input().split())), reverse=True)
print(0) if len(H) - K <= 0 else print(sum(H[K:]))