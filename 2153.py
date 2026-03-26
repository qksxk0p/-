import math
word = input()
total = 0
for c in word:
    if c.islower():
        total += ord(c) - ord('a') + 1
    else:
        total += ord(c) - ord('A') + 27
for i in range(2, int(math.sqrt(total)) + 1):
    if total % i == 0:
        print('It is not a prime word.')
        break   
else:
    print('It is a prime word.')