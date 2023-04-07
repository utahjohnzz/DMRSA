# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:12:56 2023

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
plt.plot(abang,indexb,label='B Coordinates, DMRSA',color='r',marker='s')
plt.legend()
averagema=np.average(indexb)
#print('Average Moment Arm',averagema)

from tqdm import tqdm
import time
start_time = time.time()
import numpy as np
import matplotlib.pyplot as plt
import os
import openpyxl
wb=openpyxl.Workbook()
ws=wb.active


ws.append(['Length of Glenoid Offset','Glenoid Diamater','Humeral Liner Depth','Humeral Tray Offset','Humeral Medial Offset','Neck Shaft Angle','Maximum Moment Arm','Maximum Moment Arm Location','Minimum Moment Arm','Moment Arm at 60 Degrees'])
#######Function
def DMRSAmA(lgba, lgdo, lhld,lhto, lsmo, b,color):
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
    def alpha(b):
        b=b-135
        alpha=np.array(([np.cos(np.deg2rad(b)), -np.sin(np.deg2rad(b)), 0], [np.sin(np.deg2rad(b)), np.cos(np.deg2rad(b)), 0], [ 0, 0, 1]))
        return alpha



    ####################
    #Glenohumeral Joint Vectors
    #all vectors will be WRT to N coordinate system using rotational matrices
    #Pgba is static vector of glenoid offset
    
    Pgba=np.array(([0, lgba, 0])) #no need for rotation
    
    lhdp=140 #length from greater tuberosity to proximal deltoid insertion
    lhdi=(21.4)/2
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
    lgt=12.2
    indec=0
    for z in abang:
        Pgdo=np.array(nRa(z)*[0, -lgdo/2, 0]) #index vector for glenoid diameter in N coordinates
        Pgdo=Pgdo[:,1]
        Phld=nRa(z)*[0, -lhld, 0] #index vector for humeral liner depth in N coordinates
        Phld=Phld[:,1]
        
        Phto=nRa(z)*[0, -lhto, 0] #index vector for humeral tray offset in N coordinates
        Phto=Phto[:,1]
        Psmo=nRa(z)*alpha(b)*[lsmo, 0, 0] #index vector for medial humeral offset in N coordinates
        Psmo=Psmo[:,0]
        Psh=Pgdo+Phld+Phto+Psmo #this is the joint vector
        mash=Psh[0,] #give the magnitude of the joint vector in N1 coordinates
        indexpsh=np.append(indexpsh,mash) #records this
        
       
        
        #### humeral component
        #need vectors of both the humeral diameter and the humeral length
        Psi=nRa(z)*alpha(b)*[lhdi+lgt,lhdp,0] #
        maxx=Psi[0,0]
        momentarm=(maxx+mash)
        
        
        
        
        
        
        #### deltoid muscle vectors
        #locations of insertion point
        #pDI=Psi[:,0]+Psi[:,1]
        #print(pDI)

        
        zz=abs(z-60)
        if zz<1:
            masix=momentarm
            angle=z
        indexd=np.append(indexd, momentarm)   
        if momentarm>indec:
            indec=momentarm
            enc=z
    indexd=np.delete(indexd,(0,0))
    indexpsh=np.delete(indexpsh,(0,0))
    #plt.plot(abang,indexd,marker='o')
    plt.plot(abang,indexd,color=color)
    plt.title('Moment Arm of Medial Deltoid During Abduction')
    plt.xlabel('Abduction Angle (degree)')
    plt.ylabel('Moment Arm (mm)')

    #print('Maximum moment arm of',round(indec,2),'mm at',round(enc,2),'degrees')
    #print('Moment arm at minimum is',indexd[0],'and the moment arm at 60 degrees is',masix)
    mma=round(indec,2)
    mmal=round(enc,2)
    minmma=indexd[0]
    masix=masix
    return mma,mmal,minmma,masix





lgdo=[32,38,42,46]
lgba=[0, 3.5, 2.5, 4, 2.3, 6, 9.5,6.3, -2, 5.8, 8.5]
lhld=[1.25]
lhto=[0, 2.5, 5, 7.5, 10,12.5, 15, 17.5]
lsmo=[7.5, 8.5, 9.5]
b=[135,140,150,145,155]


import random
import itertools

# define the trial variables


# combine the variables into a list of tuples
all_trials = list(itertools.product(lgba, lgdo, lhld, lhto,lsmo,b))
zz=np.shape(all_trials)
# randomize the order of the trials
random.shuffle(all_trials)
# iterate over the randomized trials
# define the number of iterations
num_iterations = zz[0]

# define the interval at which to update the progress bar
progress_interval = 1
ctrials=0
# loop over the iterations
c3=0

for trial in all_trials:
    [mma,mmal,minmma,masix]=DMRSAmA(trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],'#ffe3e2')
    var=[trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],mma,mmal,minmma,masix]
    ws.append(var)
    # update the progress bar every `progress_interval` iterations
    if (c3 + 1) % progress_interval == 0:
        progress = int((c3 + 1) / num_iterations * 100)
        print(f"Progress of Onlay Modelling: {progress}%")    
    c3=c3+1
    ctrials=ctrials+1







ws.append(['Inset Configuration (Univers Revers)'])









lgdo=[33,36,39,42,45]
lgba=[0,2.5,4]
lhld=[1.25] #need this
lhto=[0,6,9,12,15]
lsmo=[0] #need this
b=[135,145,155]

# combine the variables into a list of tuples
all_trials = list(itertools.product(lgba, lgdo, lhld, lhto,lsmo,b))
zz2=np.shape(all_trials)
# randomize the order of the trials
random.shuffle(all_trials)
# iterate over the randomized trials
# define the number of iterations
num_iterations = zz2[0]

# define the interval at which to update the progress bar
progress_interval = 1
c3=0


for trial in all_trials:
    [mma,mmal,minmma,masix]=DMRSAmA(trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],'#ffb4b5')
    var=[trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],mma,mmal,minmma,masix]
    ws.append(var)
    # update the progress bar every `progress_interval` iterations
    if (c3 + 1) % progress_interval == 0:
        progress = int((c3 + 1) / num_iterations * 100)
        print(f"Progress of Inlay Modelling: {progress}%")    
    c3=c3+1
    ctrials=ctrials+1



ws.append(['Onset Configuration (Stryker ReUnion)'])

lgdo=[32,36,40]
lgba=[0, 2, 6]
lhld=[1.25]
#lhld=[4,10]###question
lhto=[4, 6, 8, 10, 12]
lsmo=[4]
b=[135]

# define the trial variables


# combine the variables into a list of tuples
all_trials = list(itertools.product(lgba, lgdo, lhld, lhto,lsmo,b))
zz=np.shape(all_trials)
# randomize the order of the trials
random.shuffle(all_trials)
# iterate over the randomized trials
# define the number of iterations
num_iterations = zz[0]

# define the interval at which to update the progress bar
progress_interval = 1

# loop over the iterations
c3=0

for trial in all_trials:
    [mma,mmal,minmma,masix]=DMRSAmA(trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],'#ff4a49')
    var=[trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],mma,mmal,minmma,masix]
    ws.append(var)
    # update the progress bar every `progress_interval` iterations
    if (c3 + 1) % progress_interval == 0:
        progress = int((c3 + 1) / num_iterations * 100)
        print(f"Progress of ReUnion Onlay Modelling: {progress}%")    
    c3=c3+1
    ctrials=ctrials+1


ws.append(['Inset Configuration (ZB Comprehensive)'])


lgdo=[36,41]
lgba=[0,1,2,3,4,4.5,6]
lhld=[1.25] #need this
lhto=[0,5,10]
lsmo=[0] #need this
b=[135]

# combine the variables into a list of tuples
all_trials = list(itertools.product(lgba, lgdo, lhld, lhto,lsmo,b))
zz2=np.shape(all_trials)
# randomize the order of the trials
random.shuffle(all_trials)
# iterate over the randomized trials
# define the number of iterations
num_iterations = zz2[0]

# define the interval at which to update the progress bar
progress_interval = 1
c3=0


for trial in all_trials:
    [mma,mmal,minmma,masix]=DMRSAmA(trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],'#ff0202')
    var=[trial[0],trial[1],trial[2],trial[3],trial[4],trial[5],mma,mmal,minmma,masix]
    ws.append(var)
    # update the progress bar every `progress_interval` iterations
    if (c3 + 1) % progress_interval == 0:
        progress = int((c3 + 1) / num_iterations * 100)
        print(f"Progress of Comprehensive Inlay Modelling: {progress}%")    
    c3=c3+1
    ctrials=ctrials+1






# create a new folder for the spreadsheet
folder_path = 'C:\Test Exports'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)









# save the workbook to the new folder
file_path = os.path.join(folder_path, 'momentarm.xlsx')
wb.save(file_path)

labels = ['Equinoxe Onlay', 'Univers Revers Inlay','ReUnion Onlay','ZB Comprehensive']

legend=plt.legend(labels, loc='upper left', fontsize='small')
lines = legend.get_lines()
lines[0].set_color('#ffe3e2')
lines[1].set_color('#ffb4b5')
lines[2].set_color('#ff4a49')
lines[3].set_color('#ff0202')

plt.show()



onsnum=zz[0]
insnum=zz2[0]
print(f"Completed modelling of {ctrials} trials")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
