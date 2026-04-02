h, m, s = map(int,input().split())
t = int(input())
h = h + (t//3600)
t = t % 3600
m = m + (t//60)
t = t % 60
s = s + t
if s >= 60:
    m = m + 1
    s = s - 60
if m >= 60:
    h = h + 1
    m = m - 60
if h >= 24:
    h = h % 24
print(h, m, s)
