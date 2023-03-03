# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:52:23 2023

@author: utah.johnson
"""
# Import time module
import time
 
# record start time
start = time.time()
###obtaining humeral head location for rotation of humerus
import stl
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math
import numpy as np
def nRa(z):
    nRa=np.array(([np.cos(np.deg2rad(z)), -np.sin(np.deg2rad(z)), 0], [np.sin(np.deg2rad(z)), np.cos(np.deg2rad(z)), 0], [ 0, 0, 1]))
    return nRa
# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
m1 = mesh.Mesh.from_file('C:/Users/utah.johnson/Desktop/STL Files/Right_humerus_bone_one-piece.stl')
#m1 = mesh.Mesh.from_file('C:/Users/utah.johnson/Desktop/STL Files/Scapula.stl')


points = np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))
index=np.array(points[0,:])
t=np.array([-index[0],-index[1],-index[2]])
m1.translate(t)



# Auto scale to the mesh size

m1.rotate([0.5,0,0],math.radians(60),[100.75, -15.91, 259.93])
npoints = np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))


rpoint= np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))
index=np.array(rpoint[0,:])

rpoint= np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))






truth1=1000
truth2=0
c2=0
c3=0
for i in rpoint:
    if i[1]<truth1:
        truth1=i[0]
m1.translate([0,1000,0])
q=np.amin(rpoint,axis=0)
c3=0
for i in rpoint:
    if q[1]==i[1]:
        minn=c3
    c3+=1
c4=0
q=np.amax(rpoint,axis=0)
for i in rpoint:
    if q[1]==i[1]:
        maxx=c4
    c4+=1
vec=rpoint[maxx]-rpoint[minn]
r=np.sqrt(vec[0]**2+vec[2]**1+vec[1]**2)
thetax=np.rad2deg(np.arccos(vec[0]/r))
thetay=np.rad2deg(np.arccos(vec[1]/r))
thetaz=np.rad2deg(np.arccos(vec[2]/r))
theta=[thetax, thetay, thetaz]
print(theta)

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m1.vectors))
scale = m1.points.flatten()


axes.auto_scale_xyz(scale-10, scale+10, scale)



pyplot.show()


[y,x]=np.shape(points)
newpoints=np.zeros((y,x))
c3=0

  






end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")