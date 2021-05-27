
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

h=(r1)/(2*r3+2*r2) #Constante led 


while x<20: #antallet af tidsskridt 
    a.append(-r2*b[x-1]/(2*r3+2*r2)-r2*c[x-1]/(2*r3+2*r2)-r2*d[x-1]/(2*r3+2*r2)+h)
    b.append(-r2*a[x-1]/(2*r3+2*r2)-r2*c[x-1]/(2*r3+2*r2)-r2*d[x-1]/(2*r3+2*r2)+h)
    c.append(-r2*a[x-1]/(2*r3+2*r2)-r2*b[x-1]/(2*r3+2*r2)-r2*d[x-1]/(2*r3+2*r2)+h)
    d.append(-r2*a[x-1]/(2*r3+2*r2)-r2*b[x-1]/(2*r3+2*r2)-r2*c[x-1]/(2*r3+2*r2)+h)
    x=x+1
    
print(a)
   
