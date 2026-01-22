#daily temperatures problem solution
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
s=[]
res=[0]*len(temperatures)
for i, temp in enumerate(temperatures):
    while s and temp>temperatures[s[-1]]:
        prev=s.pop()
        res[prev]=i-prev
    s.append(i)
print(res)