#find pivot index
nums=[1,7,3,6,5,6]
new=sum(nums)
l=0
for i in range(len(nums)):
    new-=nums[i]
    if l==new:
        print(i)
        break
    l+=nums[i]
else:
    print(-1)