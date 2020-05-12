# AC
N = int(input())
*A, = map(int, input().split())
for a in A:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            pass
        else:
            print("DENIED")
            exit()
print("APPROVED")