
x=1 #tidsskridt = 1 ikke rør 
z=1
a=[z] #q_1_0
b=[z] #q_2_0
c=[z] #q_3_0
d=[z] #q_4_0
r1=6
r2=1
r3=1

0.875
57/12

h=(r1-r2)/(2*r3) #Constante led 


while x<20: #antallet af tidsskridt 
    a.append(-b[x-1]/2-c[x-1]/2-d[x-1]/2+h)
    b.append(-a[x-1]/2-c[x-1]/2-d[x-1]/2+h)
    c.append(-a[x-1]/2-b[x-1]/2-d[x-1]/2+h)
    d.append(-a[x-1]/2-b[x-1]/2-c[x-1]/2+h)
    x=x+1
   
