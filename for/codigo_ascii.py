import os
for x in range(260):
    x=x+1
    print(x,"=",chr(x))
    if x%10==0:
        print("Valor de la X:",x)
        os.system("pause")
        
    #continue