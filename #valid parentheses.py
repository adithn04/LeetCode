#valid parentheses
s="(]"
new=[]
add={'(':')','{':'}','[':']'}
for i in s:
    if i in add:
        new.append(add[i])
    elif not new or new.pop()!=i:
        print(False)
        break
else:
    print(not new)
