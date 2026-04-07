N = int(input())
dic = {}
js = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
for i in js:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in num:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print('0', end=' ')
