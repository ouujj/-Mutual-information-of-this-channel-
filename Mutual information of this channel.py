import matplotlib.pyplot as plt
import math

q=[]
nEr=(int)(input("Number of Error: "))
for i in range(nEr):
    q.append(input("ERROR : "))
    q[i]=float(q[i])




def Entopy (ci,q):
    Color=['blue','green','orange','yellow','red']
    PX=[]
    IXY=[]
    px0=0.01
    Q=1-q
    PX.append(0)
    IXY.append(0)
    
    #H(X|Y)
    Hxy = -1*Q*math.log(Q,2)-q*math.log(q,2)
    for i in range (99):
        px1=1-px0
      

        py0=px0*Q+px1*q
        py1=px0*q+px1*Q
         #H(X)
        Hx = -1*px1*math.log(px1,2)-px0*math.log(px0,2)
        #H(Y)
        Hy = -1*py1*math.log(py1,2)-py0*math.log(py0,2)
        #I(X;Y)
        Ixy=Hy-Hxy
    
        PX.append(px0)
        IXY.append(Ixy)
        px0+=0.01

        #print(Hx , Hy , Hxy ,Ixy)

    PX.append(1)
    IXY.append(0)
    print("Error = "+str(q))
    for i in range(19):
        print()
        print("P(x): ",end="")
        for j in range(5):
            print(str(PX[(5*i)+j])+",",end="")
    print()             
    for i in range(19):
        print()
        print("I(x;y): ",end="")
        for j in range(5):
            print(str(IXY[(5*i)+j])+",",end="")    
    plt.plot(PX, IXY, color=Color[ci%5])
    print()         
    print("=======================================================================================================")
    
for i in range(nEr):
    Entopy(i,q[i])
    

plt.xlabel('P(X)')
plt.ylabel('I(X;Y)')
plt.title('Mutual information of channel')
plt.show()



























