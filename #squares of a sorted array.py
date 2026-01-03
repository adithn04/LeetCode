#squares of a sorted array
nums = [-7, -3, 2, 3, 11]
n = len(nums)
new = [0] * n

l, h = 0, n - 1
pos = n - 1

while l <= h:
    if abs(nums[l]) > abs(nums[h]):
        new[pos] = nums[l] ** 2
        l += 1
    else:
        new[pos] = nums[h] ** 2
        h -= 1
    pos -= 1
print(new)
# for i in range(len(nums)):
#     a=nums[i]**2
#     new.append(a)
# print(new)
# for i in range(len(new)):
#     for j in range(len(new)-1):
#         if new[j]>new[j+1]:
#             new[j],new[j+1]=new[j+1],new[j]
# print(new)