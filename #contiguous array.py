#contiguous array
nums = [0,1]
nsum = 0
new = {0: -1}
mlen = 0
for i in range(len(nums)):
    if nums[i] == 0:
        nsum += -1
    else:
        nsum += 1
    if nsum in new:
        mlen = max(mlen, i - new[nsum])
    else:
        new[nsum] = i
print(mlen)