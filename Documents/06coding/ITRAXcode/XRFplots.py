# Thomas Kosciuch - Reqires changing path. Simple script to plot XRF results

path1 = "/Users/thomaskosciuch/Documents/04misc/2016_bahamas/03metaanalysis/XRF2_1.txt"
#path1 = "/Users/thomaskosciuch/Documents/04misc/2016_bahamas/02_data/SSIXX.txt"

import numpy as np
import scipy as N
import gdal
import sys
import matplotlib.pyplot as pyplot


SPC1_data = np.loadtxt(path1, dtype=np.str, delimiter='\t') 

# def sum3():
#    VAR=input()
b = list(enumerate(SPC1_data[0,1:]))
print b
print "Please enter numerater:"
Y = input()+1
print "Please enter denominater:"
Z = input()+1
print "Please enter running-average value:"
N = input()

print "plotted "+ str(SPC1_data[0,Y]) + " over "+ str(SPC1_data[0,Z])

depth = SPC1_data[3:,1].astype(np.float)
X = SPC1_data[3:,Y].astype(np.float)/SPC1_data[3:,Z].astype(np.float)


runningAvg=np.convolve(X, np.ones((N,))/N, mode='valid')
runningDepth=np.convolve(depth, np.ones((N,))/N, mode='valid')

minX = np.percentile(X,2)
maxX = np.percentile(X, 98)


import matplotlib.pyplot as plt
plt.figure(figsize=(5,10))
fig = plt.scatter(X,depth,s=0.1)
fig = plt.plot(runningAvg,runningDepth)
axes = plt.gca()
axes.set_xlim([minX,maxX])

plt.xlabel("Counts per second of "+str(SPC1_data[0,Y])+" over "+str(SPC1_data[0,Z]))
plt.ylabel("Depth (mm)")
plt.gca().invert_yaxis()

plt.savefig('/Users/thomaskosciuch/Documents/temp.pdf', bbox_inches='tight')
