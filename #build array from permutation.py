#build array from permutation
nums=[0,2,1,5,3,4]
a=[]
for i in range(len(nums)):
    a.append(nums[nums[i]])
print(a)