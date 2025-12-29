#sum of unique elements
nums=[1,2,3,2]
sum=0
for i in nums:
    if nums.count(i) == 1:
        sum=sum+i
print(sum)