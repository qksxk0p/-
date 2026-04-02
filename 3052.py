a = []
for i in range(10):
    nam = int(input()) % 42
    if nam not in a:
        a.append(nam)
print(len(a))