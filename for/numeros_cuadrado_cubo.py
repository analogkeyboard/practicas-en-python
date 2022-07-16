import math

print("N\tX^2\tX^3")
for x in range(10):
    x=x+1
    print(x,"\t",int(math.pow(x,2)),"\t",int(math.pow(x,3)))