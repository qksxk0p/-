N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
nnum = sorted(num)
for i in range(N):
    print(nnum[i])