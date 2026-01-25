#largest rectangle in histogram
h=[2,1,5,6,2,3]
s=[]
area=0
h.append(0)
for i, j in enumerate(h):
    while s and h[s[-1]] > j:
        hi=h[s.pop()]
        wi=i if not s else i-s[-1]-1
        area=max(area, hi*wi)
    s.append(i)
print(area)