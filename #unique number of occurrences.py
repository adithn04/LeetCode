#unique number of occurrences
arr=[1,2]
new={}
for i in arr:
    if i in new:
        new[i] += 1
    else:
        new[i] = 1

uni=set(new.values())
if len(uni) == len(new):
    print("true")
else:
    print("false")