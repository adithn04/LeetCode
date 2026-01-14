#product of array except self
nums=[1,2,3,4]
new=[]
a=[1]*len(nums)
count=1
for i in range(len(nums)):
    new.append(count)
    count*=nums[i]
count=1
for i in range(len(nums)-1,-1,-1):
    new[i]*=count
    count*=nums[i]
    
print(new)
