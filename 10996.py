N = int(input())
for i in range(1, N*2 + 1):
    if i % 2 != 0:#홀수
        print('* '*((N + 1)//2))
    else:
        print(' '+'* '*(N//2))


