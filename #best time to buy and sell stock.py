#best time to buy and sell stock
prices=[7,6,4,3,1]
min=prices[0]
max=0
print(min)
for i in prices:
    if i<min:
        min=i
    elif i-min>max:
        max=i-min
print(max)