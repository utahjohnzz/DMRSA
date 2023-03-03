# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:55:43 2023

@author: utah.johnson
"""
#######Function
import numpy as np
import matplotlib.pyplot as plt
lgba=5 #length of glenoid offset
Pgba=np.array(([0, lgba, 0])) #no need for rotation
lgdo=32 #diameter of glenoid
lhld=18 #humeral liner depth
lhto=5.5 #humeral tray offset
lsmo=9.1 #humeral medial offset
lhdp=10 #length from greater tuberosity to proximal deltoid insertion
lhdd=158 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
b=135
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
#user granted step data based on computational speed
step=20
rom=180
#creating abduction angle range
abang=np.linspace(0,140,num=8)
#we need to iterate over the range to find the indexwise moment 
c1=0
c3=0
w=.8
Pgdo=np.zeros((1,1))
indexd=np.zeros((1,))
indexp=np.zeros((1,))
indexpsh=np.zeros((1,))
for z in abang:
    Pgdo=np.array(nRa(z)*[0, -lgdo/2, 0]) #index vector for glenoid diameter in N coordinates
    Pgdo=Pgdo[:,1]
    Phld=nRa(z)*[0, -lhld, 0] #index vector for humeral liner depth in N coordinates
    Phld=Phld[:,1]
    Phto=nRa(z)*[0, -lhto, 0] #index vector for humeral tray offset in N coordinates
    Phto=Phto[:,1]
    Psmo=nRb(z,b)*[-lsmo, 0, 0] #index vector for medial humeral offset in N coordinates
    Psmo=Psmo[:,0]
    Psh=Pgdo+Phld+Phto+Psmo
    mash=Psh[0,]
    indexpsh=np.append(indexpsh,mash)
    
    #### humeral component
    #need vectors of both the humeral diameter and the humeral length
    Psi=nRa(z)*alpha(b)*[lhdi,lhdp,0]
    maxx=Psi[0,0]+Psi[0,1]
    indexd=np.append(indexd, (maxx+mash)*w)   
    
    #elgmh=indexd-lgmhy2
    #plt.plot(abang,elgmh,label='error LGMH')
    #pflgmh=np.polyfit(abang,elgmh,2)
    lgmhopt=np.zeros((1,1))
indexd=np.delete(indexd,(0,0))
#plt.plot(abang,indexd,label='LGMH, DMRSA RM Original',marker='^',color='g')
#plt.title('Moment Arms of Lateral Deltoid in Abduction')
#plt.xlabel('Abduction Angle (Degree)')
#plt.ylabel('Moment Arm (mm)')
#optimization
plt.plot(abang,indexd,label='Dynamic Model',marker='^',color='y')

def fitment(cabb, ma):
    pf=np.polyfit(cabb,ma,3)

    fitd=np.zeros((1,1))
    yno=np.zeros((1,1))

    for i in cabb:
        fit=pf[0]*i**3+pf[1]*i**2+pf[2]*i+pf[3]
        fitd=np.append(fitd,fit)
        yn=pf[0]*i**3+pf[1]*i**2+pf[2]*i
        yno=np.append(yno,yn)
    y=np.delete(fitd,0)
    yno=np.delete(yno,0)
    return y,yno,pf    

ma=[22, 27.5, 33, 38, 43.5, 45.5, 46, 45.5]
cabb=[0, 20, 40, 60, 80, 100, 120, 140]
[y,yno,pf]=fitment(cabb,ma)
plt.plot(cabb,y)
c5=0
err=np.zeros((0,0))
nindexd=indexd
for i in cabb:
    er=abs(indexd[c5]-y[c5])
    err=np.append(err,er)
    nindexd[c5]=y[c5]+np.average(err[0:3])
    c5+=1
plt.plot(cabb,nindexd,label='New IndexD',marker='o', color='m')
plt.plot(cabb,y,label='Fitted Data',marker='s')


plt.ylim(0,65)
plt.xlim(0,140)
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper right")


























#fitment of chris's original data
import numpy as np
import matplotlib.pyplot as plt
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
plt.plot(cabb,mglhy2,marker='s',label='MGLH CR')

mgmhy2=np.delete(mgmhy2+30,0)
#plt.plot(cabb,mgmhy)
plt.plot(cabb,mgmhy2,marker='o',label='MGMH CR')

lgmhy2=np.delete(lgmhy2+20,0)
#plt.plot(cabb,lgmhy)
plt.plot(cabb,lgmhy2,marker='^',label='LGMH CR')
plt.legend()