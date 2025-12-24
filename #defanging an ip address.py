#defanging an ip address
address = "1.1.1.1"
# new = address.replace(".", "[.]")
# print(new)
new=""
for ch in address:
    if ch == ".":
        new = new + "[.]"
    else:
        new = new + ch
print(new)