#contains duplicate II
nums = [1,2,3,1,2,3]
k = 1
new = set()
for i in range(len(nums)):
    if nums[i] in new:
        print(True)
        break
    new.add(nums[i])
    if len(new) > k:
        new.remove(nums[i - k])
else:
    print(False)
# for i in range(len(nums)):
#     for j in range(i+1, min(i+k+1, len(nums))):
#         if nums[i] == nums[j]:
#             print(True)
#             break
#     else:
#         continue
#     break
# else:
#     print(False)