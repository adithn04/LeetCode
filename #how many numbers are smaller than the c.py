# how many numbers are smaller than the current number
nums=[8,1,2,2,3]
count = 0
new=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]>nums[j]:
            count+=1
    new.append(count)
    count = 0
print(new)