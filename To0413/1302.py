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
<<<<<<< HEAD:1302.py
print(dap[0])
=======
for l in dap:
    print(l)
>>>>>>> 103ecc780a31c7539353c70f48a47a54f535ed69:To0413/1302.py
