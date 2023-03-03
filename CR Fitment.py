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