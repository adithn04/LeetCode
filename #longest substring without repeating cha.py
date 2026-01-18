#longest substring without repeating characters
s="abcabcbb"
new={}
mlen=0
i=0
j=0
while j<len(s):
    if s[j] not in new:
        new[s[j]]=j
        j+=1
        mlen=max(mlen,j-i)
        # print(new)
        # print(mlen)
    else:
        i=max(new[s[j]]+1,i)
        new[s[j]]=j
        j+=1
        mlen=max(mlen,j-i)
        # print("j:", j)
        # print("i:", i)
        # print(new)
        # print("mlen:", mlen)
print(mlen)