# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 17:08:19 2023

@author: utah.johnson
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:01:05 2023

@author: utah.johnson
"""

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
lgba=5 #length of glenoid offset
Pgba=np.array(([0, lgba, 0])) #no need for rotation
lgdo=[38,36,32] #diameter of glenoid
lhld=5 #humeral liner depth
lhto=5.5 #humeral tray offset
lsmo=[15.6,7.5,9.1] #humeral medial offset
lhdp=10 #length from greater tuberosity to proximal deltoid insertion
lhdd=158 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
#user granted step data based on computational speed
step=10
rom=140
#creating abduction angle range
abang=np.linspace(0,rom,step)
#we need to iterate over the range to find the indexwise moment 
c1=0

b=[145, 155, 135]
c3=0
w=1
for j in b:
    Pgdo=np.zeros((1,1))
    indexd=np.zeros((1,))
    indexp=np.zeros((1,))
    indexpsh=np.zeros((1,))
    for z in abang:
        Pgdo=[0, -lgdo[c3]/2, 0] #index vector for glenoid diameter in N coordinates
        
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
        plt.plot(abang,indexd,label='MGLH, DMRSA RM',marker='s',color='g')
        plt.legend()
    if c3==1:
        indexd=np.delete(indexd,(0,0))
        plt.plot(abang,indexd,label='MGMH, DMRSA RM',marker='o',color='g')
        plt.legend()
    if c3==2:
        indexd=np.delete(indexd,(0,0))
        plt.plot(abang,indexd,label='LGMH, DMRSA RM',marker='^',color='g')
        plt.legend()
        plt.title('Moment Arms of Medial Deltoid in Abduction')
        plt.xlabel('Abduction Angle (Degree)')
        plt.ylabel('Moment Arm (mm)')
    
    c3=c3+1
    
    
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
plt.plot(cabb,mgmhy2,marker='o',label='MGMH CR',color='r')

lgmhy2=np.delete(lgmhy2+20,0)
#plt.plot(cabb,lgmhy)
plt.plot(cabb,lgmhy2,marker='^',label='LGMH CR',color='r')
plt.legend()

#############
cabb2=[0, 20, 40, 60, 80, 100, 120]
mglhy=[30.5, 31.5, 36.8, 42.5, 45.5, 45, 40]

pmglhy=np.polyfit(cabb2,mglhy,2)


mglhy2=np.zeros((1,1))



for i in cabb2:
    zmglhy=pmglhy[0]*i**2+pmglhy[1]*i+[[0]]
    mglhy2=np.append(mglhy2,zmglhy)

    
    
    
    
    
    
    
    
    
mglhy2=np.delete(mglhy2+30,0)
#plt.plot(cabb2,mglhy)
plt.plot(cabb2,mglhy2,marker='s',label='Otis, 2010',color='b')

plt.legend()







#previous model
from numpy import diff

z=np.array(range(0,3))
alpha=[145, 155, 135]
beta=[38, 36, 32]
zeta=[21, 18, 26]
gamma=[15.6, 7.5, 9.1]
c3=0;

for z in alpha:
    m=2.358 #mass of upper arm
    lgba= 3.6#glenoid offset
    lgdo= beta[c3] #glenoid diameter
    lhld= 50#humeral liner depth
    lhto= gamma[c3]#humeral offset
    lsmo= 8.5#humeral medial offset
    lh= 304.56#length of humerus mm
    #lhd= 
    alpha=z
    Fd=434.5 #expected middle deltoid force
    limd=19.3/2
    Fg=9.81*m*1000
    #############################
    #Setting up angular data

    #acceleration and velcity given by exp data (16,25 m/s^2), velocity=(109.42m/s)
    dtsdts=16.25*1000 #acc in mm/s^2
    dt=109.42*1000 #vel in mm/s we may not use this though.

    ma=140
    #first need arc length
    s=lh*np.deg2rad(ma) #length of humerus times the max abduction angle gives arc length
    #now we can create a kinematic simulation
    t=np.sqrt((2*s)/dtsdts) #this gives us the time it takes for abduction according to experimental data
    #need time array
    #now we need to determine step size
    step=10
    #initializes the angular data based on step size
    #we need angular acceleration
    anga=dtsdts/lh

    #with angular acceleration we can now simulate the motion
    #first need to generate a time array
    tm=np.array(np.linspace(0,t,step))
    theta=np.zeros((step))
    count=0
    for i in tm:
        theta[count]=np.rad2deg(.5*anga*i**2)
        count=count+1

    #now to implement the two data sets together
    #Example of the angle versus the time is plotted
    #plt.figure(0)
    #plt.plot(tm, theta)
    #plt.xlabel('Time (s)')
    #plt.ylabel('Angle of Abduction (degree)')

    #we also need the velocity index wise
    dtheta=diff(theta)
    dtime=diff(tm)
    dtdt=dtheta/dtime
    #this is the angular velocity
    #need to add initial condition of 0mm/s
    dtdt=np.insert(dtdt,0,0,axis=0)

    ####################################
    #we now have simulated kinematic data for abduction
    #we can now use backwards dynamics to solve for desired parameters
    #lets first look at moment at the glenoid
    #for the codes viewability sake several intermediate calculatios will be done first

    def c1(theta):
        c1=np.cos(np.deg2rad(theta))
        return c1

    def s1(theta):
        s1=np.sin(np.deg2rad(theta))
        return s1

    def c2(alpha):
        c2=np.cos(np.deg2rad(180-alpha))
        return c2

    def s2(alpha):
        s2=np.sin(np.deg2rad(180-alpha))
        return s2

    #gravitational force
    fg=9.81*m

    #now using the derived EOM
    ms=np.zeros((step,1))
    pms=np.zeros((step,1))
    ana=np.zeros((step,1))
    count2=0
    for j in theta:
        
        ##########################################
        #moment arm calculations
        z1=-lgba*s2(alpha)
        z2=-lgdo*s1(j)*s2(alpha)
        z3=-lgdo*c1(j)*c2(alpha)
        z4=-lhld*s1(j)*s2(alpha)
        z5=-lhld*c1(j)*c2(alpha)
        z6=-lhto*s1(j)*s2(alpha)
        z7=-lhto*(c1(j)*c2(alpha))
        z8=-lsmo*c2(alpha)*s2(alpha)
        z9=lsmo*s2(alpha)*c2(alpha)
        z10=-lh*(s2(alpha))**2
        z11=-lh*(c2(alpha))**2
        z12=-limd*c2(alpha)*s2(alpha)
        z13=limd*s2(alpha)*c2(alpha)
        pma=z1+z2+z3+z4+z5+z6+z6+z7+z8+z9+z1
        pms[count2]=-pma*.5
        
        count2=count2+1
    
   # if c3==0:
         #plt.plot(theta,pms,marker='s',label='MGLH, DMRSA ALG',color='y')
    #if c3==1:
        # plt.plot(theta,pms,marker='o',label='MGMH, DMRSA ALG',color='y')
   # if c3==2:
       #  plt.plot(theta,pms,marker='^',label='LGMH, LGMH ALG',color='y')
    c3 +=1
         

cabb=[0, 20, 40, 60, 80, 100, 120]
mglhy=[30, 32, 34.5, 39.5, 43, 44, 39.8]

pmglhy=np.polyfit(cabb,mglhy,3)

mglhy2=np.zeros((1,1))

for i in cabb:
    zmglhy=pmglhy[0]*i**3+pmglhy[1]*i**2+pmglhy[2]*i+pmglhy[3]
    mglhy2=np.append(mglhy2,zmglhy)
    
mglhy2=np.delete(mglhy2,0)
#plt.plot(cabb,mglhy)
#plt.plot(cabb,mglhy2,marker='<',label='Ackland ZM Trabecular',color='y')










import numpy as np
import matplotlib.pyplot as plt
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
def aRb(na):
    b=na-90
    nRa=np.array(([np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [-np.cos(np.deg2rad(b)), np.sin(np.deg2rad(b)), 0], [ 0, 0, 1]))
    return nRa
lgba=5 #length of glenoid offset
lgdo=[38,36,32] #diameter of glenoid
lhld=8 #humeral liner depth
lhto=5 #humeral tray offset
lsmo=[15.6,7.5,9.1] #humeral medial offset
lhdd=149 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
rom=180
step=1

n1=np.zeros((0,0))
n2=np.zeros((0,0))
b1=np.zeros((0,0))
b2=np.zeros((0,0))
na=[145, 155, 135]
abang=np.linspace(180-na,rom,141)
c3=0
for j in na:
    for z in abang:
        Rna=nRa(z) #A to N Matrix
        Ran=np.transpose(Rna) #N to A Matrix
        Rab=aRb(na) #B to A matrix
        Rba=np.transpose(Rab) #A to B matrix
        Rnb=Rna.dot(Rab) #B to N matrix
        Rbn=np.transpose(Rnb) #N to B matrix
        
        
        Pgha=[0,-lhld-lhto-lgdo/2,0] #this is composed of the humeral liner and the humeral tray offset
        Pghn=Rna.dot(Pgha) #converts to N
        
        
        #Ph=[lsmo+lhdi+12,-lhdd,0] #this is the humeral medial offset, the diamater of the humerus, and the insertion point in B coordinates
        Ph=[0,0,0]
        Phn=Rnb.dot(Ph)
        
        nv=Pghn+Phn
        bv=Rbn.dot(nv)
        b1=np.append(b1,bv[0])
    c3=c3+1

    

#MomentArm 1st Revision
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
lgba=5 #length of glenoid offset
Pgba=np.array(([0, lgba, 0])) #no need for rotation
lgdo=38 #diameter of glenoid
lhld=18 #humeral liner depth
lhto=5.5 #humeral tray offset
lsmo=15.6 #humeral medial offset
lhdp=10 #length from greater tuberosity to proximal deltoid insertion
lhdd=158 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
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
b=155
indec=0
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
    zz=abs(z-60)
    
    #### humeral component
    #need vectors of both the humeral diameter and the humeral length
    Psi=nRa(z)*alpha(b)*[lhdi,lhdp,0]
    maxx=Psi[0,0]+Psi[0,1]
    momentarm=(maxx+mash)
    minv=np.linalg.inv(nRa(z))*np.linalg.inv(alpha(b))
    momentarm=minv[:,0]*momentarm
    momentarm=momentarm[0]
    
    if zz<1:
        masix=momentarm
        angle=z
    indexd=np.append(indexd, momentarm)   
    if momentarm>indec:
        indec=momentarm
        enc=z
indexd=np.delete(indexd,(0,0))
indexpsh=np.delete(indexpsh,(0,0))
plt.plot(abang,indexd,marker='o')
#plt.plot(abang,indexpsh)
plt.title('Moment Arm of Medial Deltoid During Abduction')
plt.xlabel('Abduction Angle (Degree)')
plt.ylabel('Moment Arm (mm)')





























plt.ylim(0,65)
plt.xlim(0,140)
legend=plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")




