#check if the sentence is panagram
sentence = "thequickbrownfoxjumpsoverthelazydog"
a={}
for i in sentence:
    if i.isalpha():
        a[i.lower()] = 1
print(a)
if len(a) == 26:
    print("panagram")
else:
    print("not panagram")

# for i in sentence:
#     if i in a:
#         a[i] += 1
#     else:
#         a[i] = 1
# print(a)
# if len(a) == 26:
#     print("panagram")
# else:
#     print("not panagram")