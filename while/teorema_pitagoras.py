import math
x=1
y=1
z=0
while(x<=50):
    z=int(math.sqrt(x*x+y*y))
    while(z<=50 and y<=50):
        if(z*z==(x*x+y*y)):
            print(z,"\t",x,"\t",y)
        y=y+1
        z=int(math.sqrt(x*x+y*y))
    x=x+1
    y=x