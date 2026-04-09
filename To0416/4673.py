nist = []
num = 0
split = 0
for i in range(1, 10001):
    nist.append(i)
def suyul():
        for i in range(1, 10001):
            num = 0
            split = 0
            if i < 10:
                 num+=(2*i)
            else:
                for j in str(i):
                    split+=int(j)
                num+= i + split
            if num in nist:
                nist.remove(num)
        for i in nist:
            print(i)
suyul()