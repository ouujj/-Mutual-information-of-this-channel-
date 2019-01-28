import matplotlib.pyplot as plt
import math


q=input("ERROR : ")
q=float(q)
px0=0.01
PX=[]
IXY=[]

for i in range (99):
    px1=1-px0
    Q=1-q

    py0=px0*Q+px1*q
    py1=px0*q+px1*Q

    #H(X,Y)
    Hxy = -1*px0*Q*math.log(px0*Q,2)-q*px1*math.log(px1*q,2)
    #H(X)
    Hx = -1*px1*math.log(px1,2)-px0*math.log(px0,2)
    #H(Y)
    Hy = -1*py1*math.log(py1,2)-py0*math.log(py0,2)
    #I(X;Y)
    Ixy=Hx+Hy-Hxy
    
    PX.append(px0)
    IXY.append(Ixy)
    px0+=0.01

    #print(Hx , Hy , Hxy ,Ixy)
for i in range(20):
    print()
    print("P(x): ",end="")
    for j in range(5):
        print(str(PX[j*i+i])+",",end="")
print()         
print("=======================================================================================================")      
for i in range(20):
    print()
    print("I(x;y): ",end="")
    for j in range(5):
        print(str(IXY[j*i+i])+",",end="")    
plt.plot(PX, IXY, color='orange')
plt.xlabel('P(X)')
plt.ylabel('I(X;Y)')
plt.title('Mutual information of channel with error'+str(q))
plt.show()



























