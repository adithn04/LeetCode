#maximum average subarray I
nums=[1,12,-5,-6,50,3]
k=4
new=0
for i in range(len(nums)):
    new+=nums[i]
    if i>=k:
        new-=nums[i-k]
    if i>=k-1:
        avg=new/k
        if i==k-1:
            a=avg
        else:
            a=max(a,avg)
print(a)