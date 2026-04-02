C = int(input())
for i in range(C):
    count = 0
    score = 0
    Case = list(map(int, input().split()))
    N = Case[0]
    for j in range(N):
        avg = 0
        score += Case[j + 1]

    avg = score / N

    for j in range(N):
        if Case[j + 1] > avg:
            count += 1
    print(f"{100 * (count / N):.3f}%")