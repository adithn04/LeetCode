#next greater element II
nums=[1,2,1]
n=len(nums)
res=[-1]*n
s=[]
for i in range(2*n):
    val=nums[i%n]
    while s and nums[s[-1]] < val:
        new=s.pop()
        res[new]=val
    if i<n:
        s.append(i)
print(res)