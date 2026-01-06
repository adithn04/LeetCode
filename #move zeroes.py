#move zeroes
nums = [0,1,0,3,12]
a=0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[a] = nums[i]
        a += 1
for i in range(a, len(nums)):
    nums[i] = 0
print(nums)