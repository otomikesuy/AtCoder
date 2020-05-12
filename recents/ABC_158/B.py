# AC
N, A, B = map(int, input().split())
AB = A+B
if N % (AB) == 0:
    print(N//(AB) * A)
elif N % (AB) < A:
    print(N//(AB) * A + N % (AB))
else:
    print((N//(AB) + 1) * A)