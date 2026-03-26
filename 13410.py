N, K = map(int, input().split())
res = 0
for i in range(1, K+1):
    num = str(N * i)
    rev = ''
    for j in num:
        rev = j + rev
    res = max(res, int(rev))
print(res)