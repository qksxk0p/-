N, M = map(int, input().split())
d = set()
b = set()
db = set()
for i in range(M + N):
    if len(d) != N:
        d.add(input())
    else:
        b.add(input())
for j in d:
    if j in b:
        db.add(j)
print(len(db))
for k in sorted(db):
    print(k)
