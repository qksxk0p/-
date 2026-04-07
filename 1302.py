N = int(input())
dict = {}
for i in range(N):
    book = input()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1
res = 0
for j in dict:
    res = max(res, dict.get(j))
dap = []
for k in sorted(dict):
    if res == dict.get(k):
        dap.append(k)
for l in dap:
    print(l)