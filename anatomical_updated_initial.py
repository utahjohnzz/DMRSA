# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:44:17 2023

@author: utahj
"""
import numpy as np
#######anatomical parameters include
#d2 is center of glenoid to lateral greater tuberosity
#d12 is humeral head center to lateral greater tuberosity
#d13 is humeral head center to top of greater tuberosity
#dh is diamater of humerus

import numpy as np
import matplotlib.pyplot as plt
#rotational matrices
#z is theta
#b is the neck angle
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
def aRb(b):
    bz=180-b
    
    aRb=np.array(([-np.cos(np.deg2rad(bz)), np.sin(np.deg2rad(bz)), 0], [-np.sin(np.deg2rad(bz)), -np.cos(np.deg2rad(bz)), 0], [0, 0, 1]))
    return aRb
def nRb(z,b):
    nRa=np.array(([np.cos(np.deg2rad(z)), np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    bz=180-b
    aRb=np.array(([-np.cos(np.deg2rad(bz)), np.sin(np.deg2rad(bz)), 0], [-np.sin(np.deg2rad(bz)), -np.cos(np.deg2rad(bz)), 0], [0, 0, 1]))
    nRb=aRb*nRa
    return nRb
def aRn(z):
    aRn=np.array(([np.cos(np.deg2rad(z)), np.sin(np.deg2rad(z)), 0], [-np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return aRn
def alpha(b):
    b=b-135
    alpha=np.array(([np.cos(np.deg2rad(b)), -np.sin(np.deg2rad(b)), 0], [np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [ 0, 0, 1]))
    return alpha


lgdo=42
lgba=3.5
lhld=8
lhto=5
lsmo=8.5
b=135

####################
#Glenohumeral Joint Vectors
#all vectors will be WRT to N coordinate system using rotational matrices
#Pgba is static vector of glenoid offset



lhdp=10 #length from greater tuberosity to proximal deltoid insertion

#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=90
abang=np.linspace(0,abrange,step)
#we need to iterate over the range to find the indexwise moment 
c1=0
Pgdo=np.zeros((1,1))
indexd=np.zeros((1,))
indexp=np.zeros((1,))
indexpsh=np.zeros((1,))
indec=0
lhd=42.3/2
lhi=10
d14=12.2
lgt=10
indexd=np.zeros((1,))
for z in abang:
    Pgba=np.array(([lgba,0, 0])) #n coordinates
    Pgdo=np.array(nRa(z)*[0, -lgdo/2, 0]) #index vector for glenoid diameter in N coordinates
    Pgdo=Pgdo[:,1]
    Phld=nRa(z)*[0, -lhld, 0] #index vector for humeral liner depth in N coordinates
    Phld=Phld[:,1]
    Phto=nRa(z)*[0, -lhto, 0] #index vector for humeral tray offset in N coordinates
    Phto=Phto[:,1]
    Psmo=nRb(z,b)*[-lsmo, 0, 0] #index vector for medial humeral offset in N coordinates
    Psmo=Psmo[:,0]
       
    #### humeral component
    Phi=nRa(z)*alpha(b)*[0,-lhi,0]
    Phi=Phi[:,1]
    Phd=nRa(z)*alpha(b)*[lhd,0,0]
    Phd=Phd[:,0]
    Pgt=nRa(z)*alpha(b)*[lgt,0,0]
    Pgt=Pgt[:,0]
    indexd2=Pgba+Pgdo+Phld+Psmo+Phi+Phd+Pgt
    indexdz=indexd2[0]
    indexd=np.append(indexd,indexdz)
    
    
    
    
    
    
    
    
    
    
    

indexd=np.delete(indexd,0)
    #need vectors of both the humeral diameter and the humeral length
   #Psi=nRa(z)*alpha(b)*[lhdi,lhdp,0]
   #maxx=Psi[0,0]+Psi[0,1]
   #momentarm=(maxx+mash)
   #if zz<1:
      # masix=momentarm
     #  angle=z
  # indexd=np.append(indexd, momentarm)   
  # if momentarm>indec:
  #     indec=momentarm
  #     enc=z
#indexd=np.delete(indexd,(0,0))
#indexpsh=np.delete(indexpsh,(0,0))
#indexdb2=np.delete(indexdb2,(0,0))
plt.plot(abang,indexd,marker='o')
#plt.plot(abang,indexdb2,color='red')
plt.title('Moment Arm of Medial Deltoid During Abduction')
plt.xlabel('Abduction Angle (degree)')
plt.ylabel('Moment Arm (mm)')

#print('Maximum moment arm of',round(indec,2),'mm at',round(enc,2),'degrees')
#print('Moment arm at minimum is',indexd[0],'and the moment arm at 60 degrees is',masix)
#ma=round(indec,2)
#mal=round(enc,2)
#inmma=indexd[0]
#asix=masix

