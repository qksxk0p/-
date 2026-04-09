M = int(input())
N = int(input()) #M<=N
def suyul(A):
    if A < 2:
        return False
    for i in range(2, int(A**0.5) + 1):
        if A % i == 0:
            return False #소수X
    return True  #소수
total = 0
mini = 0
for i in range(M, N + 1):
    if suyul(i) == True:
        total += i
    if mini == 0:
        mini = i
if total == 0:
    print('-1')
else:
    print(total)
    print(mini)