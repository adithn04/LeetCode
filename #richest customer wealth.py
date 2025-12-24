#richest customer wealth
a=[[1,5],[7,3],[3,5]]
count=0
sum=0
for i in a:
    for j in i:
        sum=sum+j
    if sum>count:
        count=sum
    sum=0
print(count)