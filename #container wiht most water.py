#container wiht most water
height = [1,8,6,2,5,4,8,3,7]
l, r =0, len(height)-1
maxa=0
while l<r:
    a=min(height[l],height[r])*(r-l)
    # maxa=max(maxa,a)
    # print("maxa:",maxa)
    # print(a)

    if height[l]<height[r]:
        l+=1
    else:
        r-=1
print(maxa)