#koko eating bananas
import math
piles=[3,6,7,11]
h=8
l=1
r=max(piles)
while l<r:
    mid=(l+r)//2
    hr=0
    for i in piles:
        hr+=math.ceil(i/mid)
    if hr<=h:
        r=mid
    else:
        l=mid+1
print(l)