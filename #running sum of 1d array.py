#running sum of 1d array
nums =[1,2,3,4]
new=[]
sum=0
for i in nums:
    sum=sum+i
    new.append(sum)
print(new)