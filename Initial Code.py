#MomentArm 1st Revision
import numpy as np
import matplotlib.pyplot as plt
import os
import openpyxl
wb=openpyxl.Workbook()
ws=wb.active

path = os.path.join(os.path.expanduser("~"), "Desktop", "Test Exports", "MomentArm.xlsx")



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
b=135
#user granted step data based on computational speed
step=91
#creating abduction angle range
abrange=180
bz=b-90
abang=np.linspace(0,abrange,step)
#we need to iterate over the range to find the indexwise moment 
indexd=np.zeros((0,0))
indexz=np.zeros((0,0))

r1m=38/2
r2m=20
r3m=0
r4m=20
r5m=55
r6m=10 #15
r7m=0 #9
for z in abang:
    
    #GH Joint
    r1=[r1m/2, 0, 0] #Glenoid Application to Glenoid Interface
    
    r2=nRa(z)*[0, -r2m, 0] #Resection Plane to Articular Surface
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
    
    r6=[r6m,0,0] # horizontal distance from COR to Acromion outer portion
    r7=[0,r7m,0] #vertical distance from COR to Acromion outer portion
    
    
    
    
    indexd=np.append(indexd,n1)
    

plt.plot(abang,indexd)





