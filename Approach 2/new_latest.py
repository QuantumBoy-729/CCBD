from __future__ import division 
import math
import turtle
import random
import time
pointer=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('white')
pointer.shape("arrow")
pointer.color("white")
pointer.width(1.1)
#pointer.goto(0,0)
pointer.speed(100)
#equation=[]
color=["green","red","blue","orange","black","yellow"]
#random

start = time.time()
#intersection
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C
def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return [x,y]
    else:
        return False

def inter(equation,i,k):
    p=0
    #print(len(equation))
    if(len(equation)>=2):
        for j in range(0,len(equation)-1):
            L1=line(equation[j][0],equation[j][1])
            L2=line(i,k)
            R = intersection(L1, L2)
            if(R):
                distance_1=math.sqrt((i[0]-k[0])**2+(i[1]-k[1])**2)
                distance_2=math.sqrt((i[0]-R[0])**2+(i[1]-R[1])**2)
                if(R==i):
#                    print(0)
                    return 0
                
                if(distance_1>distance_2):
#                    print(distance_1,distance_2)
#                    print(R)
#                    print([equation[j][0],equation[j][1]],[i,k],j)
                    #print(1)
#                    print(1)
                    return 1
    #print(0)
    return 0
def checkquadrant(a,b):
    if (a[0]>b[0] and a[1]>b[1]):
        return 1
    elif (a[0]<b[0] and a[1]>b[1]):
        return 2
    elif (a[0]<b[0] and a[1]<b[1]):
        return 3
    elif (a[0]>b[0] and a[1]<b[1]):
        return 4
    elif (a[1]==b[1]):
        if (a[0]>b[0]):
            return 5 #0
        else:
            return 6 #180
        
    elif (a[0]==b[0]):
        if (a[1]>b[1]):
            return 7 #90
        else:
            return 8 #270
sum=0

new=[]
x0=0
y0=0
plot=[]
for k in range(0,6):
    ran=[]
    
    for i in range(0,(10-k)*10):
        x=random.randint(-100,100)
        y=random.randint(-100,100)
        while((x0-x)**2 < 1000  ):
            x0=x
            x=random.randint(-(10-k)*10,(10-k)*10)
        while((y0-y)**2 < 1000 ):
            y0=y
            y=random.randint(-(10-k)*10,(10-k)*10)
        ran.append([x,y])
        x0=x
        y0=y
    plot.append(ran)



def find_area_perim(new):
    a = 0
    p = 0
    ox,oy = new[0]
    for x,y in new[1:]:
        a += (x*oy-y*ox)
        p += abs((x-ox)+(y-oy)*1j)
        ox,oy = x,y
    return a/2,p   
dimensions=[]

cen=[]
def centroid(array):
    xaxis=0
    yaxis=0
    for i in range(0,len(array)):
        xaxis=array[i][0]+xaxis
        yaxis=array[i][1]+yaxis

    xaxis=xaxis/len(array)
    yaxis=yaxis/len(array)
    return xaxis,yaxis
ends=[]
def endpoints(mid,array):
    x1,y1=mid[0],mid[1]
    x2,y2=mid[0],mid[1]
    x3,y3=mid[0],mid[1]
    x4,y4=mid[0],mid[1]
    for i in array:
        if (i[0] > mid[0] and i[1] >mid[1]):
            x1=i[0]
            y1=i[1]
        elif(i[0] < mid [0] and i[1] > mid[1]):
            x2=i[0]
            y2=i[1]
        elif(i[0] < mid [0] and i[1] < mid[1]):
            x3=i[0]
            y3=i[1]
        else:
            x4=i[0]
            y4=i[1]
    ends.append([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])



points_new=[[[1.81,11.23],[ 18.41 ,69.81999999999999],[ 22.42, 92.19], [24.18 ,30.65],[ 47.47 ,90.33],[ 48.98, 84.06999999999999],[ 69.18000000000001, 43.04], [99.92 ,34.4], [51.1 ,1.53], [40.72 ,14.39], [1.81, 11.23]],[[10.3 ,29.74], [27.22, 56.87], [46.11, 66.89],[ 49.61, 72.75], [68.48, 74.36], [75.20999999999999 ,87.81999999999999],[ 82.87 ,85.56999999999999], [84.81999999999999, 73.45], [86.79000000000001 ,58.28], [99.03 ,24.49], [19.56 ,5.74], [10.3 ,29.74]],[[7.41 ,66.93000000000001], [11.12 ,99.22], [18.73, 72.48999999999999], [95, 88.53], [98.05, 77.06], [89.59 ,53.08], [85.19 ,61.03], [82.01000000000001 ,53.15], [81.51000000000001, 14.68], [43.68, 47.78], [33.96 ,22.93], [18.28 ,42.79], [7.41 ,66.93000000000001]],[[0.24, 57.37], [9.08, 91.29000000000001], [24.93 ,67.41], [30.05, 58.46], [42.54, 54.66], [46.9 ,54.56], [78.77 ,48.43], [68.45 ,46.67], [65.8 ,8.550000000000001], [31.04 ,53.75], [26.02, 18.25], [21.69 ,6.19], [12.28 ,21.54], [0.24 ,57.37]]]
"""for f in range(0,3):
    ran=plot[f]
    new=[]
    k=[ran[0][0],ran[0][1]]
    pointer.color(color[f])
    pointer.goto(ran[0][0],ran[0][1])
    equation=[]"""
for f in range(0,len(points_new)):
    ran=points_new[f]
    new=[]
    k=[ran[0][0],ran[0][1]]
    pointer.color("white")
    pointer.goto(ran[0][0],ran[0][1])
    pointer.color(color[f])
    
    equation=[]
    for i in range(1,len(ran)):
        
        sum=sum+1
#        print(1)
        distance=math.sqrt(((ran[i][0]-k[0])**2)+((ran[i][1]-k[1])**2))
        top=k[1]-ran[i][1]
        bottom=k[0]-ran[i][0]
        q=checkquadrant(ran[i],k)
        if q==1 or q==4:
            angle=math.atan(top/bottom)*180/math.pi
        #pointer.left(angle)
        elif q==2:
            angle=math.atan(top/bottom)*180/math.pi
            angle=angle+180
        #pointer.left(angle)
        elif q==3:
            angle=math.atan(top/bottom)*180/math.pi
            angle=180+angle
        #pointer.left(angle)
        elif q==5:
            angle=0
        #pointer.left(angle)
        elif q==6:
            angle=180
        #pointer.left(angle)
        elif q==7:
            angle=90
        #pointer.left(angle)
        else:
            angle=270
        #pointer.left(angle)
    #equation.append([i,k])
        l=0
    #print(equation)   
        a=inter(equation,ran[i],k)
        if(a==0):
            pointer.left(angle)
            pointer.forward(distance)
            pointer.left(-angle)
            kp=[[ran[i][0],ran[i][1]],[k[0],k[1]]]
            equation.append(kp)
            k[0]=ran[i][0]
            k[1]=ran[i][1]
            new.append(ran[i])
    pointer.goto(ran[0][0],ran[0][1])
    area=find_area_perim(new)
    
    qw=centroid(new)
    cen.append(qw)
     
    endpoints(qw,new)


    
    dimensions.append(area)
    #print(angle)
#pointer.goto(new[0][0],new[0][1])
#pointer.goto(0,0)
for i in range(0,2):
    print(dimensions[i],cen[i],ends[i])    

    #print(i,k)
"""o=[ran[0][0],ran[0][1]]   
x=True
j=len(new)-1
while(x and j!=1):
    q=inter(equation,new[j],o)
    if(q==0):
        pointer.goto(new[0][0],new[0][1])
        x=True
    else:
        pointer.color("black")
        pointer.goto(new[j-1][0],new[j-1][1])
        pointer.color("red")
    j=j-1   
if(j==1):
    print("not found")"""

end = time.time()
print(end-start)


