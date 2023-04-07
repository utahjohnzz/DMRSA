# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:51:15 2023

@author: utah.johnson
"""

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
r3m=-5
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
    r3=r3[:,0]
    
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
plt.plot(abang,indexb,label='B Coordinates, DMRSA',color='r',marker='s')
plt.legend()
averagema=np.average(indexb)
#print('Average Moment Arm',averagema)
