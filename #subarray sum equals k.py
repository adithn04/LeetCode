#subarray sum equals k
nums = [1,2,3]
k = 3
new = {0: 1}
su = 0
count = 0
for num in nums:
    su += num
    if su - k in new:
        count += new[su - k]
        new[su] = new.get(su, 0) + 1
print(count)