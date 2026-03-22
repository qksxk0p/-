now = 0
maxp = 0
for i in range(4):
    g, c = map(int,input().split())
    now = now - g + c
    maxp = max(maxp, now)
print(maxp)
