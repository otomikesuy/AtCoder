# AC after contest
S = input()[::-1]
remain_table = [0] * 2019
remain_table[0] = 1
d = 1
chk = 0
for s in S:
    chk += int(s) * d
    chk = chk % 2019
    remain_table[chk] += 1
    d *= 10
    d %= 2019

ans = 0
for r in remain_table:
    ans += r * (r - 1) // 2
print(ans)