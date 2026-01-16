#maximum subarray
nums=[-2,1,-3,4,-1,2,1,-5,4]
max_=nums[0]
nsum=0
for i in nums:
    nsum+=i
    if nsum>max_:
        max_=nsum
        print(max_)
    if nsum<0:
        nsum=0
        print(nsum)
print(max_)
