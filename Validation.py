# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:35:07 2023

@author: utah.johnson
"""
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

def fitment(cabb, ma):
    pmglhy=np.polyfit(cabb,ma,3)

    mglhy2=np.zeros((1,1))

    for i in cabb:
        zmglhy=pmglhy[0]*i**3+pmglhy[1]*i**2+pmglhy[2]*i+pmglhy[3]
        mglhy2=np.append(mglhy2,zmglhy)
        
    y=np.delete(mglhy2,0)
    #plt.plot(cabb,mglhy)
    return y
    #more chris  
    
    
    
    
    
    
    
    
    
    
    
###validation v ackland
cabb=[0, 20, 40, 60, 80, 100, 120]
ma=[30, 32, 34.5, 39.5, 43, 44, 39.8]

#Ackland
y=fitment(cabb,ma)
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(cabb,y,label='Ackland ZIM-BIO Trabecular',marker='<',color='r')
plt.legend()
#grammont
#ma=[26, 31, 36.5, 42, 44, 45.5, 45]
#y=fitment(cabb,ma)
#plt.figure(1)
#plt.subplot(2,1,2)
#plt.plot(cabb,y,label='Grammont',marker='<',color='r')

#ma=[22.5, 25, 28, 32, 36, 39.5, 40.5]
#y=fitment(cabb,ma)
#plt.figure(1)
#plt.subplot(2,1,2)
#plt.plot(cabb,y,label='DJO',marker='<',color='r')





















































plt.legend()
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")