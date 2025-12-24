#shuffle the array
nums=[2,5,1,3,4,7]
n=3
a=[]
for i in range(n):
    a.append(nums[i])
    a.append(nums[i+n])
print(a)