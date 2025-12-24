#kids with the greatest number of candies
candies=[2,3,5,1,3]
extraCandies=3
max_candies=max(candies)
result=[]
for i in range(len(candies)):
    if candies[i]+extraCandies >= max_candies:
        result.append(True)
    else:
        result.append(False)
print(result)