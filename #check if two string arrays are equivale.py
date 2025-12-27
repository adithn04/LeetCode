#check if two string arrays are equivalent
word1=["ab","c"]
word2=["a","bc"]
a=""
b=""

for i in range(len(word1)):
    a+=word1[i]
for i in range(len(word2)):
    b+=word2[i]
if a==b:
    print(True)
else:
    print(False)
