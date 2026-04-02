N = int(input())
result = N
count = 0
while True:
    a = result // 10
    b = result % 10
    new = a + b
    result = (10 * b) + (new % 10)
    count += 1
    if result == N:
        break
print(count)
