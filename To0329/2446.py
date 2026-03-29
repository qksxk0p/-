N = int(input())
sp = 0
for i in range(2 * N - 1, 2, -2):
    print(' ' *  sp , '*' * i,sep='')
    sp += 1
for j in range(1, 2*N, 2):
    print(' '*sp, '*' * j, sep='')
    sp -= 1
