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




# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.set_xlabel('X axis')
axes.set_ylabel('Y axis')
axes.set_zlabel('Z axis')
m1 = mesh.Mesh.from_file('C:/Users/utahj/STL FILES/Right_humerus_Cut_2_top.stl')
#m1 = mesh.Mesh.from_file('C:/Users/utah.johnson/Desktop/STL Files/Scapula.stl')

points = np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))
index=np.array(points[0,:])
t=np.array([-index[0],-index[1],-index[2]])
m1.translate(t)



# Auto scale to the mesh size

#m1.rotate([0.5,0,0],math.radians(0),[100.75, -15.91, 259.93])
npoints = np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))









end = time.time()
#############################


# Calculate the centroid point
centroid = np.mean(m1.vectors.reshape(-1, 3), axis=0)
t=[-centroid[0],-centroid[1],-centroid[2]]
m1.translate(t)
# Print the result
#print('Centroid point:', centroid)


#m1.rotate([0.5,0,0],math.radians(0),[centroid[0], centroid[1], centroid[2]])

newpoints = np.array(np.around(np.unique(m1.vectors.reshape([int(m1.vectors.size/3), 3]), axis=0),2))
##############################
mx=0
my=0
mz=0
mex=100
mey=100
mez=100
for i in newpoints:
    if i[0]>mx:
        mx=i[0]
    if i[0]<mex:
        mex=i[0]
    if i[1]>my:
        my=i[1]
    if i[0]<mey:
        mey=i[1]
    if i[2]>mz:
        mz=i[2]
    if i[0]<mez:
        mez=i[2]
    
maxp=[mx,my,mz]
minp=[mex,mey,mez]






# Define the height threshold to cut off the mesh
height_threshold = 2

# Find the heights of all triangles in the mesh
triangle_heights = np.mean(m1.vectors[:, :, 2], axis=1)

# Extract the triangles below the height threshold
cut_triangles = m1.vectors[triangle_heights < height_threshold]
cut_vertices = np.concatenate(cut_triangles)
cut_faces = np.arange(len(cut_vertices)).reshape(-1, 3)
cut_mesh_collection = mplot3d.art3d.Poly3DCollection(cut_vertices[cut_faces], alpha=0.25)





















###############################
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m1.vectors))
scale = m1.points.flatten()


axes.auto_scale_xyz(scale-10, scale+10, scale)

pyplot.show()




print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")