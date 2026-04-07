N = int(input())
for i in range(N):
    test = input()
    count = 0
    combo = 0
    for j in test:
        if j == 'O':
            combo += 1
            count += combo
        else:
            combo = 0
    print(count)
