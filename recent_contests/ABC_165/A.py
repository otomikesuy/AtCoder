# AC
K = int(input())
A, B = map(int, input().split())
ans = 1
for i in range(100000):
    ans = i * K
    if A <= ans and ans <= B:
        print("OK")
        exit()
print("NG")

# Model answer
K = int(input())
A, B = map(int, input().split())
largest = b // k * k
if A <= largest:
    print("OK")
else:
    print("NG")