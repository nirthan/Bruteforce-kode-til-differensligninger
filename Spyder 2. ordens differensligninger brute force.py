
x=2 #tidsskridt = 1 ikke rør 
z_1=40
z_2=50
a=[z_1,z_2] #q_1_0
b=[z_1,z_2] #q_2_0
c=[z_1,z_2] #q_3_0
d=[z_1,z_2] #q_4_0
e=[z_1,z_2]
r1=60
r2=9
r3=2500

h=(r3-r1)/(2*r2) #Constante led 


while x<100: #antallet af tidsskridt
    a.append(-b[x-1]/4-c[x-1]/4-d[x-1]/4+h-b[x-2]/4-c[x-2]/4-d[x-2]/4-e[x-1]/4-e[x-2]/4)
    b.append(-a[x-1]/4-c[x-1]/4-d[x-1]/4+h-a[x-2]/4-c[x-2]/4-d[x-2]/4-e[x-1]/4-e[x-2]/4)
    c.append(-a[x-1]/4-b[x-1]/4-d[x-1]/4+h-a[x-2]/4-b[x-2]/4-d[x-2]/4-e[x-1]/4-e[x-2]/4)
    d.append(-a[x-1]/4-b[x-1]/4-c[x-1]/4+h-a[x-2]/4-b[x-2]/4-c[x-2]/4-e[x-1]/4-e[x-2]/4)
    #d.append(0)
    #e.append(0)
    e.append(-a[x-1]/4-b[x-1]/4-c[x-1]/4-d[x-1]/4+h-a[x-2]/4-b[x-2]/4-c[x-2]/4-d[x-2]/4)
    x=x+1
   
    
print(a)
