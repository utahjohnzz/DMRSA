# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:12:56 2023

@author: utah.johnson
"""




#######Function
def DMRSAmA(lgba, lgdo, lhld,lhto, lsmo, b):
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
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas import DataFrame 
    lhdp=10 #length from greater tuberosity to proximal deltoid insertion
    lhdi=42.3/2 #diameter of humeral bone
    #user granted step data based on computational speed
    step=20
    rom=180
    #creating abduction angle range
    abang=np.linspace(0,140,num=140)
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
    mgmhopt=np.zeros((1,1))
    lgmhopt=np.zeros((1,1))
    mglhopt=np.zeros((1,1))
    for k in abang:
        lgmhoptz=-0.00473208*k**2+0.388335*k+2.19905
        lgmhopt=np.append(lgmhopt,lgmhoptz)
    lgmhopt=np.delete(lgmhopt, 0)
    lgmhoptd=indexd-lgmhopt
    for k in abang:
        mgmhoptz=-0.00441676*k**2+0.410809*k+-8.70313
        mgmhopt=np.append(mgmhopt,mgmhoptz)
    mgmhopt=np.delete(mgmhopt, 0)
    mgmhoptd=indexd-mgmhopt
    for k in abang:
        mglhoptz=-0.00351516*k**2+0.20214*k-2.80163
        mglhopt=np.append(mglhopt,mglhoptz)
    mglhopt=np.delete(mglhopt, 0)
    mglhoptd=indexd-mglhopt
    c5=0
    aw=np.zeros((1,1))
    for k in abang:
        awz=(mglhoptd[c5]+mgmhoptd[c5]+lgmhoptd[c5])/3
        aw=np.append(aw,awz)
        c5+=1
    aw=np.delete(aw,0)
    exp=[abang,aw]
    df=DataFrame({'Abduction Angle':abang,'Moment Arm':aw})
    df.to_excel(r'C:\Users\utah.johnson\Desktop\Test Exports\Test2.xlsx', sheet_name='sheet1',index=False)
    return exp
    
        
    
    
    #plt.figure(1)
    #plt.subplot(2,1,1)
    #plt.plot(abang,lgmhoptd,label='LGMH',marker='o', color='b')
    #plt.plot(abang,mgmhoptd,label='MGMH',marker='s', color='r')
    #plt.plot(abang,mglhoptd,label='MGLH',marker='^', color='m')
    #plt.plot(abang,aw,label='Optimized',marker='^', color='y')
    #plt.legend()
    
    
DMRSAmA(0,38, 20,5, 15.6, 135)
    

