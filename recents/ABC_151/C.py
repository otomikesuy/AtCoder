# AC (review)
N, M = map(int, input().split())
prb = [0 for x in range(N)]
ac_cnt = 0
wa_cnt = 0
for x in range(M):
    p, s = input().split()
    if prb[int(p) - 1] == 0:
        if s == "WA":
            wa_cnt += 1
        else:
            ac_cnt += 1
            prb[int(p) - 1] = 1
    else:
        pass
print(ac_cnt, wa_cnt)