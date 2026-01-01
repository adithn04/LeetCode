#binary search
nums=[-1,0,3,5,9,12]
x=9
l=0
h=len(nums)-1
for i in range(len(nums)):
    m=l+(h-l)//2
    if nums[m]==x:
        print(m)
        break
    elif nums[m]<x:
        l=m+1
    else:
        h=m-1
else:
    print(-1)