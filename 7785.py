n = int(input())
s = set()
for i in range(n):
    a, b = input().split()
    if b == 'enter':
        s.add(a)
    else:
        s.discard(a)
res = sorted(s, reverse=True)
for i in res:
    print(i)