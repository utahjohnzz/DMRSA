#MomentArm 1st Revision
import numpy as np
import matplotlib.pyplot as plt



# Import time module
import time
 
# record start time
start = time.time()
 
 


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
lgdo=32 #diameter of glenoid
lhld=30 #humeral liner depth
lhto=5.5 #humeral tray offset
lsmo=9.5 #humeral medial offset
lhdp=97 #length from greater tuberosity to proximal deltoid insertion
lhdd=158 #length from greater tuberosity to distal deltoid insertion
lhdi=42.3/2 #diameter of humeral bone
#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=140
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
    
    #### humeral component
    #need vectors of both the humeral diameter and the humeral length
    Psi=nRa(z)*alpha(b)*[lhdi,lhdp,0]
    maxx=Psi[0,0]+Psi[0,1]
    momentarm=(maxx+mash)*.7
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
# record end time
print('Maximum moment arm of',round(indec,2),'mm at',round(enc,2),'degrees')
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")


