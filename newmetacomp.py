# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:33:59 2023

@author: utah.johnson
"""
#new metacompt
#MomentArm 1st Revision
import numpy as np
import matplotlib.pyplot as plt
#rotational matrices
#z is theta
#b is the neck angle
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
def alpha(b):
    b=b-90
    alpha=np.array(([np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [-np.cos(np.deg2rad(b)), np.sin(np.deg2rad(b)), 0], [ 0, 0, 1]))
    return alpha



####################
#Glenohumeral Joint Vectors
#all vectors will be WRT to N coordinate system using rotational matrices
#Pgba is static vector of glenoid offset
b=145
b2=b
#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=140
bz=b2-90
rthm=1.8 #how much GH:Scapular
ghm=abrange-abrange/((1+rthm)/rthm) #how much purely GH rotation occurs
abang=np.linspace(0,ghm+bz,step)

#we need to iterate over the range to find the indexwise moment 
indexd=np.zeros((0,0))
indexb=np.zeros((0,0))

r1m=38/2
r2m=20
r3m=0
r4m=30
r5m=60
r6m=29.9 #15
r7m=33.9 #9
ho=15.6
for z in abang:
    
    #GH Joint
    r1=[0, 0, 0] #Glenoid Application to Glenoid Interface
    
    r2=nRa(z)*[0, -ho, 0] #Resection Plane to Articular Surface
    r2=r2[:,1]
    
    r3=nRa(z)*[r3m, 0, 0] #Superior/Inferior Placement of Tray
    r3=r3[:,1]
    
    r4=nRa(z)*alpha(b)*[r4m,0,0] #IM Axis to insertion
    r4=r4[:,0]
    r5=nRa(z)*alpha(b)*[0,-r5m,0] #Resection plane to location of insertion
    r5=r5[:,1]
    n1=r1[0]+r2[0]+r3[0]+r4[0]+r5[0] #moment arm in N coordinates
    n2=r1[1]+r2[1]+r3[1]+r4[1]+r5[1] #moment arm in N coordinates
    n=np.array([n1,n2,0])
    print(n1)
    #=[r6m,0,0] # horizontal distance from COR to Acromion outer portion
    #r7=[0,r7m,0] #vertical distance from COR to Acromion outer portion
    acr=[r6m,r7m,0]
    #b1=n1*np.cos(np.deg2rad(z-bz))
    #indexb=np.append(indexb,b1)
    mf=abs(acr-n)
    
    beta=np.rad2deg(np.arctan(mf[1]/mf[0]))
    zeta=90-beta
    bm=n1*np.cos(np.deg2rad(zeta))
    indexd=np.append(indexd,n1)
    indexb=np.append(indexb,bm)
    
    
abang=np.linspace(0,abrange,step)
#plt.plot(abang,indexd,label='N Coordinates, DMRSA',color='r',marker='o')
plt.plot(abang,indexb,label='MGLH DMRSA',color='r',marker='s')
plt.legend()
averagema=np.average(indexb)
#print('Average Moment Arm',averagema)



#new metacompt
#MomentArm 1st Revision
import numpy as np
import matplotlib.pyplot as plt
#rotational matrices
#z is theta
#b is the neck angle
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
def alpha(b):
    b=b-90
    alpha=np.array(([np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [-np.cos(np.deg2rad(b)), np.sin(np.deg2rad(b)), 0], [ 0, 0, 1]))
    return alpha



####################
#Glenohumeral Joint Vectors
#all vectors will be WRT to N coordinate system using rotational matrices
#Pgba is static vector of glenoid offset
b=155
b2=b
#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=140
bz=b2-90
rthm=1.8 #how much GH:Scapular
ghm=abrange-abrange/((1+rthm)/rthm) #how much purely GH rotation occurs
abang=np.linspace(0,ghm+bz,step)

#we need to iterate over the range to find the indexwise moment 
indexd=np.zeros((0,0))
indexb=np.zeros((0,0))

r1m=38/2
r2m=20
r3m=0
r4m=30
r5m=60
r6m=29.9 #15
r7m=33.9 #9
ho=7.5
for z in abang:
    
    #GH Joint
    r1=[0, 0, 0] #Glenoid Application to Glenoid Interface
    
    r2=nRa(z)*[0, -ho, 0] #Resection Plane to Articular Surface
    r2=r2[:,1]
    
    r3=nRa(z)*[r3m, 0, 0] #Superior/Inferior Placement of Tray
    r3=r3[:,1]
    
    r4=nRa(z)*alpha(b)*[r4m,0,0] #IM Axis to insertion
    r4=r4[:,0]
    r5=nRa(z)*alpha(b)*[0,-r5m,0] #Resection plane to location of insertion
    r5=r5[:,1]
    n1=r1[0]+r2[0]+r3[0]+r4[0]+r5[0] #moment arm in N coordinates
    n2=r1[1]+r2[1]+r3[1]+r4[1]+r5[1] #moment arm in N coordinates
    n=np.array([n1,n2,0])
    print(n1)
    #=[r6m,0,0] # horizontal distance from COR to Acromion outer portion
    #r7=[0,r7m,0] #vertical distance from COR to Acromion outer portion
    acr=[r6m,r7m,0]
    #b1=n1*np.cos(np.deg2rad(z-bz))
    #indexb=np.append(indexb,b1)
    mf=abs(acr-n)
    
    beta=np.rad2deg(np.arctan(mf[1]/mf[0]))
    zeta=90-beta
    bm=n1*np.cos(np.deg2rad(zeta))
    indexd=np.append(indexd,n1)
    indexb=np.append(indexb,bm)
    
    
abang=np.linspace(0,abrange,step)
#plt.plot(abang,indexd,label='N Coordinates, DMRSA',color='r',marker='o')
plt.plot(abang,indexb,label='DMRSA MGMH',color='b',marker='o')
plt.legend()
averagema=np.average(indexb)
#print('Average Moment Arm',averagema)

#new metacompt
#MomentArm 1st Revision
import numpy as np
import matplotlib.pyplot as plt
#rotational matrices
#z is theta
#b is the neck angle
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
def alpha(b):
    b=b-90
    alpha=np.array(([np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [-np.cos(np.deg2rad(b)), np.sin(np.deg2rad(b)), 0], [ 0, 0, 1]))
    return alpha



####################
#Glenohumeral Joint Vectors
#all vectors will be WRT to N coordinate system using rotational matrices
#Pgba is static vector of glenoid offset
b=135
b2=b
#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=140
bz=b2-90
rthm=1.8 #how much GH:Scapular
ghm=abrange-abrange/((1+rthm)/rthm) #how much purely GH rotation occurs
abang=np.linspace(0,ghm+bz,step)

#we need to iterate over the range to find the indexwise moment 
indexd=np.zeros((0,0))
indexb=np.zeros((0,0))

r1m=38/2
r2m=20
r3m=0
r4m=30
r5m=60
r6m=29.9 #15
r7m=33.9 #9
ho=9.1
for z in abang:
    
    #GH Joint
    r1=[0, 0, 0] #Glenoid Application to Glenoid Interface
    
    r2=nRa(z)*[0, -ho, 0] #Resection Plane to Articular Surface
    r2=r2[:,1]
    
    r3=nRa(z)*[r3m, 0, 0] #Superior/Inferior Placement of Tray
    r3=r3[:,1]
    
    r4=nRa(z)*alpha(b)*[r4m,0,0] #IM Axis to insertion
    r4=r4[:,0]
    r5=nRa(z)*alpha(b)*[0,-r5m,0] #Resection plane to location of insertion
    r5=r5[:,1]
    n1=r1[0]+r2[0]+r3[0]+r4[0]+r5[0] #moment arm in N coordinates
    n2=r1[1]+r2[1]+r3[1]+r4[1]+r5[1] #moment arm in N coordinates
    n=np.array([n1,n2,0])
    print(n1)
    #=[r6m,0,0] # horizontal distance from COR to Acromion outer portion
    #r7=[0,r7m,0] #vertical distance from COR to Acromion outer portion
    acr=[r6m,r7m,0]
    #b1=n1*np.cos(np.deg2rad(z-bz))
    #indexb=np.append(indexb,b1)
    mf=abs(acr-n)
    
    beta=np.rad2deg(np.arctan(mf[1]/mf[0]))
    zeta=90-beta
    bm=n1*np.cos(np.deg2rad(zeta))
    indexd=np.append(indexd,n1)
    indexb=np.append(indexb,bm)
    
    
abang=np.linspace(0,abrange,step)
#plt.plot(abang,indexd,label='N Coordinates, DMRSA',color='r',marker='o')
plt.plot(abang,indexb,label='DMRSA LGMH',color='g',marker='^')
plt.legend()
averagema=np.average(indexb)
#print('Average Moment Arm',averagema)





























cabb=[0, 20, 40, 60, 80, 100, 120, 140]
mglhy=[30, 36, 41, 45.5, 58.5, 58.5, 56.5, 41.5]
mgmhy=[30, 36, 43.5, 48, 51.5, 53, 52.5, 48]
lgmhy=[22, 27.5, 33, 38, 43.5, 45.5, 46, 45.5]
pmglhy=np.polyfit(cabb,mglhy,2)
pmgmhy=np.polyfit(cabb,mgmhy,2)
plgmhy=np.polyfit(cabb,lgmhy,2)


mglhy2=np.zeros((1,1))
mgmhy2=np.zeros((1,1))
lgmhy2=np.zeros((1,1))


for i in cabb:
    zmglhy=pmglhy[0]*i**2+pmglhy[1]*i+[[0]]
    mglhy2=np.append(mglhy2,zmglhy)
    
    zmgmhy=pmgmhy[0]*i**2+pmgmhy[1]*i+[[0]]
    mgmhy2=np.append(mgmhy2,zmgmhy)
    
    zlgmhy=plgmhy[0]*i**2+plgmhy[1]*i+[[0]]
    lgmhy2=np.append(lgmhy2,zlgmhy)
    
    
    
    
    
    
    
    
    
    
mglhy2=np.delete(mglhy2+30,0)
#plt.plot(cabb,mglhy)
plt.plot(cabb,mglhy2,marker='s',label='MGLH CR',color='r')

mgmhy2=np.delete(mgmhy2+30,0)
#plt.plot(cabb,mgmhy)
plt.plot(cabb,mgmhy2,marker='o',label='MGMH CR',color='b')

lgmhy2=np.delete(lgmhy2+20,0)
#plt.plot(cabb,lgmhy)
plt.plot(cabb,lgmhy2,marker='^',label='LGMH CR',color='g')
plt.legend()

#############
cabb2=[0, 20, 40, 60, 80, 100, 120]
mglhy=[30.5, 31.5, 36.8, 42.5, 45.5, 45, 40]

pmglhy=np.polyfit(cabb2,mglhy,2)


mglhy2=np.zeros((1,1))







