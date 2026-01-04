#reverse string
s=["h","e","l","l","o"]

# Method 1: Using two-pointer approach
l=0
h=len(s)-1
while l<h:
    s[l],s[h]=s[h],s[l]
    l+=1
    h-=1
print(s)

#method 2: Using built-in reverse function
# s.reverse()
# print(s)

# Method 3: Using slicing
# s=s[::-1]
# print(s)