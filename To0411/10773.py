K = int(input())
count = 0
nums = []
for i in range(K):
    add = int(input())
    if add != 0:
        nums.append(add)
    else:
        nums.pop()
for j in range(len(nums)):
    count += nums[j]
print(count)
