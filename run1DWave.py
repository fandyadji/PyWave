# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:51:08 2020

@author: Fandy Adji
Main Program for Solving 1D Acoustic Wave Equation Based on 2nd Order Finite Difference
An Exercise to Create 1D Wave Propagation Simulation
"""

from config import Parameter
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

param = Parameter()
dx = param.xmax/(param.nx-1) 
isrc = param.sx #Source Location
t0 = 4. / param.freq

#SOURCE TIME FUNCTION
src = np.zeros(param.nt + 1)
time = np.linspace(0 * param.dt, param.nt * param.dt, param.nt)
src  = -2. * (time - t0) * (param.freq ** 2) * (np.exp(-1.0 * (param.freq ** 2) * (time - t0) ** 2))

#Initialize Empty Pressure
p    = np.zeros(param.nx) #Pressure (Now)
pold = np.zeros(param.nx) #Pressure (Past)
pnew = np.zeros(param.nx) #Pressure (Present)
d2px = np.zeros(param.nx) #2nd Space Derivative of p

#Model Initialization
c = np.zeros(param.nx)
c = c + param.c0

#Coordinate Initialization
x = np.arange(param.nx)
x = x * dx 


#1D Wave Propagation Solution (Homogeneus Case With Finite Difference)
seis=[]
for it in range(1,param.nt):
    for i in range(1, param.nx-1):
        d2px[i] = (p[i+1] - 2 * p[i] + p[i-1]) / dx ** 2
    
    pnew = 2 * p - pold + c ** 2 * param.dt ** 2 * d2px
    
    pnew[isrc] = pnew[isrc] + src[it] / (dx) * param.dt ** 2
    seis.append(pnew[param.gx])
    
    pold, p = p, pnew
    print("Time Step: {}s".format(it*param.dt))
    if it % param.snap == 0 or it == 1:
        plt.plot(x,(pnew),'-b')
#        plt.xlim(0,np.max(x))
        plt.xlim(0,3000)
        #plt.ylim(-0.000025,0.000025)
        plt.xlabel("Distance (m)")
        plt.ylabel("Pressure")
        plt.savefig("Time{}".format(it))
        plt.close()

plt.plot(time[:-1],seis)
    