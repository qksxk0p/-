n = int(input())
dots = list(map(int, input().split()))
dots.sort()
a = 0
ans = 0
for i in range(n):
    ans += dots[i]*i - a
    a += dots[i]
print(ans * 2)
