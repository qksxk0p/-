N = int(input())
def suyul(A):
    if A < 100:
        return True
    else:
        three = list(map(int, str(A)))
        if three[2] - three[1] == three[1] - three[0]:
            return True
        else:
            return False
count = 0
for i in range(1, N + 1):
    if suyul(i) == True:
        count += 1
    else:
        pass
print(count)