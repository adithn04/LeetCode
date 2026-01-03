arm=153
a=arm
n=len(str(a))
tot=0

while a>0:
    b=a%10
    tot+=b**n
    a=a//10
    
if arm==tot:
    print("Armstrong number")
else:
    print("nrml number")