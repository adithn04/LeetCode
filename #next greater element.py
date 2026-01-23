#next greater element
nums1=[4,1,2]
nums2=[1,3,4,2]
s=[]
next_={}
for i in nums2:
    while s and i > s[-1]:
        b=s.pop()
        next_[b] = i
    s.append(i)
for i in s:
    next_[i]=-1
a=[next_[i] for i in nums1]
print(a)