#valid palindrome
s = "race a car"
new=[]
for i in s:
    if i.isalnum():
        new.append(i.lower())
for i in range(len(new)):
    if new[i] != new[len(new)-1-i]:
        a = "Not a palindrome"
        break
    else:
        a = "Palindrome"
print(a)