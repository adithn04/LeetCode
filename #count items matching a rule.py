#count items matching a rule
items = [["phone","blue","pixel"],
        ["computer","silver","lenovo"],
        ["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
ruleKeyIndex = {"type": 0, "color": 1, "name": 2}[ruleKey]
count = 0
for i in items:
    if i[ruleKeyIndex] == ruleValue:
        count += 1
print(count)
