#logest repeating character replacement
s="ABAB"
k=2

l=0
co={}
res=0
maxf=0

for i in range(len(s)):
    co[s[i]]=1+co.get(s[i],0)
    # print(co)
    # print(co[s[i]])
    maxf=max(maxf,co[s[i]])

    while (i-l+1)-maxf>k:
        co[s[l]]-=1
        l+=1
    res=max(res,i-l+1)

print(res)