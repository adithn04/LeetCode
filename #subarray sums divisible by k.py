#subarray sums divisible by k
nums=[4,5,0,-2,-3,1]
k=5
rem={0:1}
pre=0
new=0
for i in nums:
    pre+=i
    re = pre%k

    if re in rem:
        new+=rem[re]
    rem[re]=rem.get(re,0)+1
print(new)