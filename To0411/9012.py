T = int(input())

for j in range(T):
    vps = []
    come = input()
    for i in come:
        if i == '(':
            vps.append(i)
        else:
            if not vps:
                print('NO')
                break
            vps.pop()
    if vps:
        print('NO')
    else:
        print('YES')
