K, L = map(int,input().split())
dic = {}
for i in range(L):
    st = input()
    dic[st] = i
for j in range(K):
    print(dic.keys[j])
