# -*- coding: utf-8 -*-
"""
@author: Utah Johnson


Code:
I believe every important line of code has notes next to it. Refer to external documentation for more extensive description of the code.
"""

def DMRSAmA(b,abrange,r1m,r2m,r3m,r4m,r5m,r6m, r7m,r8m,r9m,tb,rc,rca):
        
    ###############Initial Setup
    import numpy as np #library for math functions
    import matplotlib.pyplot as plt #library for plotting
    #rotational matrices
    #z is theta
    #b is the neck angle
    def nRa(z): #this converts N to A coordinates as a function of the abduction angle
        z=np.deg2rad(z) #converts to radians
        nRa=np.array(([np.cos(z), -np.sin(z), 0], 
                      [np.sin(z), np.cos(z), 0], 
                      [ 0, 0, 1])) #this was found by hand
        return nRa #returns the rotational matrix at that specific angle
    def alpha(b): #this converts B to A coordinates as a function of the neck angle
        b=b-90 #required for rotation matrix calculation
        b=np.deg2rad(b) #converts to radians
        alpha=np.array(([np.sin(b), np.cos(b), 0], 
                        [-np.cos(b), np.sin(b), 0], 
                        [ 0, 0, 1])) #this was found by hand
        return alpha #returns the rotational matrix at that specific neck angle
    def mbh(mf,dwn,bm,dwm,z): #this is the muscle behavior function that decides which moment arm to use in the case deltoid wrapping exists at the abduction angle
        momentarm=bm #initially it just assumes the moment arm is without deltoid wrapping
        if mf[0]<dwn[0]: #this detects if the vector that relates to the deltoid insertion intersects the vector of the greater tuberosity
            momentarm=dwm #if there is interesection, deltoid wrapping is confirmed and the moment arm is changed
        return momentarm 

    #####################Initialization
    step=90 #user granted step data based on computational speed
    #creating abduction angle range
    bz=b-90 #refer to documentation
    rthm=1.8 #how much GH:Scapular
    ghm=abrange-abrange/((1+rthm)/rthm) #how much purely GH rotation occurs
    abang=np.linspace(0,ghm+bz,step) #refer to documentation
    #we need to iterate over the range to find the indexwise moment 
    indexd=np.zeros((0,0)) #sets up vector to append to
    indexb=np.zeros((0,0)) #sets up vector to append to
    indexw=np.zeros((0,0)) #sets up vector to append to
    indexm=np.zeros((0,0)) #sets up vector to append to
    
    ######################GH Joint
    for z in abang: #abuction range for the glenohumeral joint
        r1=np.array([r1m, 0, 0]) #Glenoid Application to Glenoid Interface     
        r2=nRa(z)*[0,-r2m, 0] #Resection Plane to Articular Surface
        r2=r2[:,1] #extracts just the N coordinates from the 3x3 matrix
        r3=nRa(z)*[r3m, 0, 0] #Superior/Inferior Placement of Tray
        r3=r3[:,0] #extracts just the N coordinates from the 3x3 matrix
        r4=nRa(z)*alpha(b)*[r4m,0,0] #IM axis to the deltoid insertion
        r4=r4[:,0] #extracts just the N coordinates from the 3x3 matrix
        di=tb-rc/np.sin(np.deg2rad(rca-90)) #takes the length from the top of the humerus to the insertion and subtracts the resection depth
        
        r5=nRa(z)*alpha(b)*[0,-di,0] #Resection plane to location of insertion 
        r5=r5[:,1] #extracts just the N coordinates from the 3x3 matrix
        n1=r1[0]+r2[0]+r3[0]+r4[0]+r5[0] #moment arm in N coordinates
        n2=r1[1]+r2[1]+r3[1]+r4[1]+r5[1] #moment arm in N coordinates
        n=np.array([n1,n2,0]) #creates a vector for the N coordinates
        acr=[r6m-r9m,r7m,0] #position of the acromion crest (deltoid origin) in relation to the COR. Allows for offset of the COR (see documentation)
        mf=abs(acr-n) #Vector for the line of action for the deltoid
        beta=np.rad2deg(np.arctan(mf[1]/mf[0])) #Part of the hand derived geometric relationship to find the moment arm
        zeta=90-beta #angle from the COR to the perpindicular vector of the muscle line of action
        bm=n1*np.cos(np.deg2rad(zeta)) #calculated the magnitude of the moment arm WRT to the N1 coordinate    
        indexd=np.append(indexd,n1) #appends to the vector
        indexb=np.append(indexb,bm) #appends to the vector

        #######################Deltoid Wrapping.
        r8=nRa(z)*alpha(b)*[r8m,0,0] #this is the vector that relates the IM axis at the resection plane to the greater tuberosity in the A coordinate
        r8=r8[:,0] #extracts just the N coordinates from the 3x3 matrix
        dwn=np.array([(r1[0]+r2[0]+r3[0]+r8[0]),(r1[1]+r2[1]+r3[1]+r8[1]),0]) #this finds the vector from the COR to the outside edge of the greater tuberosity
        #with that vector, we can now find the line of action for the delotid when considering deltoid wrapping
        mladw=acr-dwn #uses vector math to relate the found vector from the COR to the greater tuberosity to the origin of the deltoid at the acromion
        rho=np.rad2deg(np.arctan(mladw[1]/mladw[0])) #finds the angle of this vector WRT to the original N coordinate system
        if rho<0: #this next part is required because I found that due to trignometric relationships magnitudes which switch to negative between two data points and thus would cause the moment arm to be negative randomly.
            rho=rho*-1 #this just corrects it and has no effect on the moment arm magnitude
        phi=90-rho #finds the angle of the vector that relates the COR to the perpindicular line of action of the deltoid wrapping muscle vector
        dwm=n[0]*np.cos(np.deg2rad(phi)) #this is the deltoid wrapping moment arm found from the original N1 magnitude
        indexw=np.append(indexw,dwm) #appends to vector
        momentarm=mbh(mf, dwn, bm, dwm,z) #this uses the muscle behavior function to figure out which moment arm philospophy is appropriate
        indexm=np.append(indexm,momentarm) #appends to vector
        

    ##############Post processing
    posproc=np.zeros((0,0)) #refer to documentation  
    pf=np.polyfit(abang,indexm,3) #fits a third degree polynomial to the choppy muscular behavior results
    for i in abang: #goes through each abduction angle data point
        indexm2=pf[0]*i**3+pf[1]*i**2+pf[2]*i**1+pf[3] #fits the data
        posproc=np.append(posproc,indexm2) #post processing
        
        #this method has the same magnitude error, but typically may vary indice wise towards the end of the abduction range.
    maxa=max(posproc)
    abang=np.linspace(0,abrange,step) #this is required to reset the abduction range for plotting purposes
    
    countf=0 #starts a 0 counter
    for angle in abang: #iterates through entire abduction range
        #print(abs(angle-90))
        if abs(angle-90)<=.5: #this finds the data point at the 90 degree angle
            nina=posproc[countf] #calculates the moment arm at the 90th degree in the abduction range
            break #stops the loop once it is found
        countf+=1
    maz=posproc[0] #moment arm at 0
    avm=np.average(posproc) #average moment arm
    countz=0
    for i in posproc: #this will find the maximum moment arm via t/f thresholding
        if abs(i-maxa)<.01:
            indexmom=countz
            maxl=abang[countz]
            break
        countz+=1
    countz=0
    for i in indexm: #this will find the moment at which the moment arm switches from one philospophy ot another via looking at the magnitude of change between adjacent poi
        if countz==89:
            swl=0 #it will show 0 if no switch occurs
            break
        if abs(i-indexm[countz+1])>1:
            swl=abang[countz]
            break
        countz+=1
        
    return abang,indexb,indexw,indexm,posproc,nina,maz,avm,maxa,maxl,swl #this is the returned values



"""
return abang,indexb,indexw,indexm,posproc,nina,maz,avm,maxa,maxl,swl #this is the returned values
This is the return command is returns these values that were calculated in the function. In order these represent:
1. abang - Abduction Range (Degrees of Abduction)
2. indexb - Vector of Moment Arms for Non-Deltoid Wrapping Algorithm
3. indexw - Vector of Moment Arms for Deltoid Wrapping Algorithm
4. indexm - Vector of Moment Arms for Muscle Behavior (Integrated) Algorithm
5. posproc - Vector of Moment Arms for Fitted Muscle Behavior (Integrated) Algorithm
6. nina - Moment Arm @ 90 Degrees
7. maz - Moment Arm @ 0 Degrees
8. avm - Average Moment Arm
9. maxa - Maximum Moment Arm
10. maxl - Maximum Moment Arm Angle Location
11. swl - Angle Location at which Moment Arm Switches from Non-Deltoid Wrapping to Deltoid Wrapping Model via Muscle Behavior
"""

    

"""
You can delete this next section of code but I left it in as a template to know how to plot and activate the function. None of this is part of the calculation/the function itself.
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6), facecolor='black')
#DMRSAmA(b,abrange,r1m,r2m,r3m,r4m,r5m,r6m, r7m,r8m,r9m,tb,rc) This is how the function is called
[abang,indexb,indexw,indexm,posproc,nina,maz,avm,maxa,maxl,swl]=DMRSAmA(135,140,32/2,15,0,21.4/2,40,29, 33,46.8/2+20,3.9,100,30,135) #This calls the function with the specified parameters and outputs the values as each variable listed in the left hand side.
plt.plot(abang,indexb,label='No Deltoid Wrapping') #Plots no-deltoid wrapping moment arm
plt.plot(abang,indexw,label='Deltoid Wrapping') #Plots deltoid wrapping moment arm
plt.plot(abang,indexm,label='Muscle Behavior') #Plots MB unprocessed
plt.plot(abang,posproc,label='Muscle Behavior, Post Processed') #Plots fitted MB
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.ylim(0,80) #x limits
plt.xlim(0,140) #y limits
plt.xlabel('Abduction Angle (degree)', fontsize=12)
plt.ylabel('Moment Arm (mm)', fontsize=12)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.tick_params(top=False, right=False)
plt.axvline(x=90, color='magenta', linestyle='--')
ax = plt.gca()  # get the current axes
ax.set_facecolor('black')
ax.grid(color='gray', linestyle='--')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
plt.legend(facecolor='black', fontsize=12)
legend = ax.legend(facecolor='black',bbox_to_anchor=(1.04, 1), loc="upper left")
maz=round(maz,2)
nina=round(nina,2)
avm=round(avm,2)
maxa=round(maxa,2)
maxl=round(maxl,2)
swl=round(swl,2)
text = f'Moment Arm at 0 Degrees: {maz}'
plt.text(142, 50, text, fontsize=12, color='white')
text1 = f'Moment Arm at 90 Degrees: {nina}'
text2 = f'Average Moment Arm: {avm}'
text3 = f'Maximum Moment Arm: {maxa}'
text4 = f'Maximum Moment Arm Location: {maxl}'
text5 = f'Location of Moment Arm Switch: {swl}'
plt.text(142, 44, text1, fontsize=12, color='magenta')
plt.text(142, 38, text2, fontsize=12, color='white')
plt.text(142, 32, text3, fontsize=12, color='white')
plt.text(142, 26, text4, fontsize=12, color='white')
plt.text(142, 20, text5, fontsize=12, color='white')
