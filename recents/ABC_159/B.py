# AC
S = input()
l = len(S)
fl = (l-1)//2
sl = (l+3)//2 - 1
f = S[:fl]
s = S[sl:]
if f == f[::-1] and s == s[::-1] and S == S[::-1]:
    print('Yes')
else:
    print('No')