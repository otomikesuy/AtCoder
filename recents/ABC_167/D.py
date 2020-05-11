# AC after contest
N, K = map(int, input().split())
A = list(map(int, input().split()))
journey = [1]
dup = {}
for i in range(N+100000):
    journey.append(A[journey[-1] - 1])

end_idx, start_idx = 0, 0
dup = {}
for i, j in enumerate(journey):
    if j in dup:
        end_idx = i
        break
    else:
        dup[j] = 0
for i, j in enumerate(journey):
    if j == journey[end_idx]:
        start_idx = i
        break

if K <= start_idx:
    print(journey[K])
    exit()
b = end_idx - start_idx
m = (K - start_idx) % b
print(journey[start_idx + m])
