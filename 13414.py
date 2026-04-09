import sys
K, L = map(int,sys.stdin.readline().split())
dic = {}
for i in range(L):
    st = str(sys.stdin.readline())
    dic[st] = i
dic = sorted(dic.items(), key=lambda x: x[1])
K = min(K, len(dic))
for j in range(K):
    sys.stdout.write(dic[j][0])