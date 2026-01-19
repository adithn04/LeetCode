#longest palindrome
s="abccccdd"
new={}
for i in s:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
# print(new)
# print(new.items())
# print(new)
count=0
odd=0
for j in new:
    # print(j)
    # print(new[j])
    if new[j]%2==0:
        count+=new[j]
    else:
        count+=new[j]-1
        odd=1
print(count+odd)
