# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:32:18 2023

@author: utahj
"""

def DMRSAmA(b,abrange,r1m,r2m,r3m,r4m,r5m,r6m, r7m,r8m,r9m):
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
    def mbh(mf,dwn,bm,dwm):
        momentarm=bm
        if mf[0]<dwn[0]:
            momentarm=dwm
        return momentarm


    ####################
    #Glenohumeral Joint Vectors
    #all vectors will be WRT to N coordinate system using rotational matrices
    #Pgba is static vector of glenoid offset
    b2=b
    #user granted step data based on computational speed
    step=90
    #creating abduction angle range
    bz=b2-90
    rthm=1.8 #how much GH:Scapular
    ghm=abrange-abrange/((1+rthm)/rthm) #how much purely GH rotation occurs
    abang=np.linspace(0,ghm+bz,step)
    #if b==155:
        #abang=np.linspace(0,ghm+bz-20,step)
    #we need to iterate over the range to find the indexwise moment 
    indexd=np.zeros((0,0))
    indexb=np.zeros((0,0))
    indexw=np.zeros((0,0))
    indexm=np.zeros((0,0))
    #=9.1

    for z in abang:

        #GH Joint
        r1=np.array([r1m, 0, 0]) #Glenoid Application to Glenoid Interface
        #r1=nRa(z)*np.array([0,-r1m, 0]) #Glenoid Application to Glenoid Interface
       
        #r1=r1[:,1]
        
        #r2=np.array([r2m, 0, 0])
        r2=nRa(z)*[0,-r2m, 0] #Resection Plane to Articular Surface
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
        
        #=[r6m,0,0] # horizontal distance from COR to Acromion outer portion
        #r7=[0,r7m,0] #vertical distance from COR to Acromion outer portion
        acr=[r6m-r9m,r7m,0]
    
        
        #b1=n1*np.cos(np.deg2rad(z-bz))
        #indexb=np.append(indexb,b1)
        mf=abs(acr-n)
        
        beta=np.rad2deg(np.arctan(mf[1]/mf[0]))
        zeta=90-beta
        bm=n1*np.cos(np.deg2rad(zeta))
        beta=np.rad2deg(np.arcsin(bm/np.sqrt(n1**2+n2**2)))
        
        indexd=np.append(indexd,n1)
        indexb=np.append(indexb,bm)
        if z==0:
            abdz=bm
        qua=z-60
        if qua<1:
            abdsix=bm
            
        #Deltoid Wrapping.
        #first to find the vector from the COR to the lateral edge of the humeral resection
        #we already have the vector to the resection in the form of r1, r2
        #we now need to find the distance from the axis of the prosthesis altered by r3 to the edge of the lateral humerus.
        #we now need to incorporate an anatomy vector that is the distance from the IM canal to the lateral humerus.
        r8=nRa(z)*[r8m,0,0]
        r8=r8[:,0]
        dwn=np.array([(r1[0]+r2[0]+r3[0]+r8[0]),(r1[1]+r2[1]+r3[1]+r8[1]),0])
        
        #with that vector, we can now find the line of action for the delotid when considering deltoid wrapping
        mladw=acr-dwn
        rho=np.rad2deg(np.arctan(mladw[1]/mladw[0]))
        if rho<0:
            rho=rho*-1
        phi=90-rho
        dwm=n1*np.cos(np.deg2rad(phi))
        
        #print('z:',z,'mladw:',mladw,'dwn:',dwn,'phi:',phi,'dwm:',dwm,'rho:',rho,'\n')
        indexw=np.append(indexw,dwm)
        
        #muscular behavior
        #print(mf[0])
        #print(mladw[0])
        momentarm=mbh(mf, dwn, bm, dwm)
        indexm=np.append(indexm,momentarm)
        


    posproc=np.zeros((0,0))
    #post processing
    pf=np.polyfit(abang,indexm,3)
    for i in abang:
        indexm2=pf[0]*i**3+pf[1]*i**2+pf[2]*i**1+pf[3]
        posproc=np.append(posproc,indexm2)
        
            

    abang=np.linspace(0,abrange,step)

    #plt.plot(abang,indexb,color='r',marker='^',label='DMRSA')
        

    #plt.plot(abang,indexd,label='N Coordinates, DMRSA',color='r',marker='o')
    #plt.plot(abang,indexb,label='No Deltoid Wrapping',color='r',marker='s',markersize=2)

    #plt.plot(abang,indexw,label='Deltoid Wrapping',color='b',marker='o')
    averagema=np.average(posproc)
    #plt.plot(abang,indexw,color='b',marker='o',markersize=2,label='Deltoid Wrapping')
    #plt.plot(abang, indexm,color='y',marker='^',label='Muscular Behavior',markersize=2)
    #plt.plot(abang,posproc,color='m',marker='s',label='Muscular Behavior, Post Processed',markersize=2)

    averagema=np.average(indexb)
    print('Average Moment Arm for Original Code',averagema)

    averagema=np.average(indexw)
    print('Average Moment Arm for Deltoid Wrapping',averagema)

    averagema=np.average(indexm)
    print('Average Moment Arm for Muscular Behavior',averagema)

    averagema=np.average(posproc)
    print('Average Moment Arm for Muscular Behavior, Post Proc',averagema)
    return abang,indexb,indexw,indexm,posproc

    


import matplotlib.pyplot as plt
import numpy as np

#[abang,indexb,indexw,indexm,posproc]=DMRSAmA(145,140,32/2,20.9,0,21.4/2,40,29, 33,46.8/2-5,3.9)
#plt.plot(abang,indexb,color='r',label='Inlay')
#plt.plot(abang,indexw,color='r')
#plt.plot(abang,indexm,color='r')
#plt.plot(abang,posproc,color='r')

print('\n')



#[abang,indexb,indexw,indexm,posproc]=DMRSAmA(145,140,32/2,26.6,0,21.4/2,40,29, 33,46.8/2-5,3.9)
#plt.plot(abang,indexb,color='b',label='Onlay')
#plt.plot(abang,indexw,color='b')
#plt.plot(abang,indexm,color='b')
#plt.plot(abang,posproc,color='b')

[abang,indexb,indexw,indexm,posproc]=DMRSAmA(145,140,32/2,20.9,0,21.4/2,40,29, 33,46.8/2-5,3.9)

res=[0,-3,3]
for i in res:
    [abang,indexb,indexw,indexm,posproc]=DMRSAmA(145,140,32/2,20.9+15,i,21.4/2,40,29, 33,46.8/2-5,3.9)
    plt.plot(abang,posproc,label=('Humeral Tray Sup/Inf Offset:',i))
   
   



plt.ylim(0,80)
plt.xlim(0,140)
plt.xlabel('Abduction Angle (degree)')
plt.ylabel('Moment Arm (mm)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

