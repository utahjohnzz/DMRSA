# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:51:40 2023

@author: utah.johnson
"""

#piecewise error function
#comparison file#MomentArm 1st Revision
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



####################
#Glenohumeral Joint Vectors
#all vectors will be WRT to N coordinate system using rotational matrices
#Pgba is static vector of glenoid offset

    
    
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
    zmglhy=pmglhy[0]*i**2+pmglhy[1]*i+pmglhy[0]
    mglhy2=np.append(mglhy2,zmglhy)
    
    zmgmhy=pmgmhy[0]*i**2+pmgmhy[1]*i+pmglhy[0]
    mgmhy2=np.append(mgmhy2,zmgmhy)
    
    zlgmhy=plgmhy[0]*i**2+plgmhy[1]*i+pmglhy[0]
    lgmhy2=np.append(lgmhy2,zlgmhy)
    

    
    
    
    
    
    
mglhy2=np.delete(mglhy2+30,0)
plt.plot(cabb,mglhy)
plt.plot(cabb,mglhy2,marker='s',label='MGLH CR',color='r')

mgmhy2=np.delete(mgmhy2+30,0)
plt.plot(cabb,mgmhy)
plt.plot(cabb,mgmhy2,marker='o',label='MGMH CR',color='r')

lgmhy2=np.delete(lgmhy2+20,0)
plt.plot(cabb,lgmhy)
plt.plot(cabb,lgmhy2,marker='^',label='LGMH CR',color='r')


lgba=7.5 #length of glenoid offset
Pgba=np.array(([0, lgba, 0])) #no need for rotation
lgdo=[42,36,32] #diameter of glenoid
lhld=25 #humeral liner depth
lhto=5.5 #humeral tray offset
lsmo=[19,7.5,9.1] #humeral medial offset
lhdp=10 #length from greater tuberosity to proximal deltoid insertion
lhdd=158 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
#user granted step data based on computational speed
step=20
rom=140
#creating abduction angle range
abang=np.linspace(0,140,num=8)
#we need to iterate over the range to find the indexwise moment 
c1=0

b=[145, 155, 135]
c3=0
w=.8
for j in b:
    Pgdo=np.zeros((1,1))
    indexd=np.zeros((1,))
    indexp=np.zeros((1,))
    indexpsh=np.zeros((1,))
    for z in abang:
        Pgdo=np.array(nRa(z)*[0, -lgdo[c3]/2, 0]) #index vector for glenoid diameter in N coordinates
        Pgdo=Pgdo[:,1]
        Phld=nRa(z)*[0, -lhld, 0] #index vector for humeral liner depth in N coordinates
        Phld=Phld[:,1]
        Phto=nRa(z)*[0, -lhto, 0] #index vector for humeral tray offset in N coordinates
        Phto=Phto[:,1]
        Psmo=nRb(z,b[c3])*[-lsmo[c3], 0, 0] #index vector for medial humeral offset in N coordinates
        Psmo=Psmo[:,0]
        Psh=Pgdo+Phld+Phto+Psmo
        mash=Psh[0,]
        indexpsh=np.append(indexpsh,mash)
        
        #### humeral component
        #need vectors of both the humeral diameter and the humeral length
        Psi=nRa(z)*alpha(b[c3])*[lhdi,lhdp,0]
        maxx=Psi[0,0]+Psi[0,1]
        indexd=np.append(indexd, (maxx+mash)*w)   
        
    if c3==0:
        indexd=np.delete(indexd,(0,0))
        #plt.plot(abang,indexd,label='MGLH, DMRSA RM Original',marker='s',color='g')
        plt.legend()
        
        #emglh=indexd-mglhy2
        #plt.plot(abang,emglh,label='error LGMH')
        #pfmglh=np.polyfit(abang,emglh,2)
        mglhopt=np.zeros((1,1))
        for k in abang:
            mglhoptz=-0.00351516*k**2+0.20214*k-2.80163
            mglhopt=np.append(mglhopt,mglhoptz)
                  
        mglhopt=np.delete(mglhopt, 0)
        mglhoptd=indexd-mglhopt
        plt.plot(abang,mglhoptd,label='MGLH, DMRSA RM Optimized',color='m',marker='s')
        
    if c3==1:
        indexd=np.delete(indexd,(0,0))
        #plt.plot(abang,indexd,label='MGMH, DMRSA RM Original',marker='o',color='g')
        plt.legend()
        
        #elgmh=indexd-mgmhy2
        #plt.plot(abang,elgmh,label='error LGMH')
        #pflgmh=np.polyfit(abang,elgmh,2)
        mgmhopt=np.zeros((1,1))
        for k in abang:
            mgmhoptz=-0.00441676*k**2+0.410809*k+-8.70313
            mgmhopt=np.append(mgmhopt,mgmhoptz)
                  
        mgmhopt=np.delete(mgmhopt, 0)
        mgmhoptd=indexd-mgmhopt
        plt.plot(abang,mgmhoptd,label='MGMH, DMRSA RM Optimized',color='m',marker='o')
        
        
        
        
    if c3==2:
        indexd=np.delete(indexd,(0,0))
        #plt.plot(abang,indexd,label='LGMH, DMRSA RM Original',marker='^',color='g')
        plt.legend()
        plt.title('Moment Arms of Medial Deltoid in Abduction')
        plt.xlabel('Abduction Angle (Degree)')
        plt.ylabel('Moment Arm (mm)')
        #elgmh=indexd-lgmhy2
        #plt.plot(abang,elgmh,label='error LGMH')
        #pflgmh=np.polyfit(abang,elgmh,2)
        lgmhopt=np.zeros((1,1))
        for k in abang:
            lgmhoptz=-0.00473208*k**2+0.388335*k+2.19905
            lgmhopt=np.append(lgmhopt,lgmhoptz)
                  
        lgmhopt=np.delete(lgmhopt, 0)
        lgmhoptd=indexd-lgmhopt
        plt.plot(abang,lgmhoptd,label='LGMH, DMRSA RM Optimized',color='m',marker='^')
    
    c3=c3+1
    
plt.legend()
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")