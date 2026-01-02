#search insert position
nums=[1,3,5,6]
target=5
l=0
h=len(nums)-1
while l<=h:
    m=(l+h)//2
    if nums[m]==target:
        print(m)
    elif nums[m]<target:
        l=m+1
    elif nums[m]>target:
        h=m-1
print(l)
