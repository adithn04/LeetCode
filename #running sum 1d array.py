#running sum 1d array
nums = [1,2,3,4]
sum = 0
new=[]
for i in nums:
    sum += i
    new.append(sum)
print(new)