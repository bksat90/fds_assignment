# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:49:24 2023

@author: bksat
"""

import numpy as np
import matplotlib.pyplot as plt


# read the data from the file
data = np.genfromtxt('data0.csv', delimiter=' ')

# max(data)
# min(data)

# distributing the weights of newborn by binning into 40 bins with equal
# widths in the range from 2.0 to 5.0 (based on max and min values)
histogram, binedge = np.histogram(data, bins=50, range=[2.0,5.0])

# finding bincentre and binwidth for each bin
bincentre = 0.5*(binedge[1:] + binedge[:-1])
binwidth = binedge[1:] - binedge[:-1]

# normalise the histogram (divide the each count in the bin by total count)
yval = histogram/np.sum(histogram)

# finding average weight of new born babies
w = np.sum(bincentre * yval)

# plotting probability density function (i.e histogram)
plt.figure(dpi=600)
plt.bar(bincentre, yval, width=0.85*binwidth,
        label = "Newborn babies distribution")
plt.xlabel('Weight of newborns', fontsize=10)
plt.ylabel('Probability', fontsize=10)
plt.title("Weight Distribution Of Newborn Babies",
          fontsize=10, fontweight="bold")

# plotting the mean value
plt.plot([w,w],[0.0,max(yval)], '--', c='red')
text = '''Average, W = {}'''.format(w.astype(float))
plt.text(x=w, y=max(yval), s=text, fontsize=10, c='red')

# finding cumulative distribution
cumul_dist = np.cumsum(yval)

# finding min index such that index for cumulative value is above 25%
min_index = 0
for val in cumul_dist:
    if val <= 0.25:
        min_index += 1

# X such that 75% of newborn babies are born with weight above X
x =  binedge[min_index]

# finding the distribution range corresponds to X
temp = []
for i in range(len(yval)):
    if i < min_index:
        temp.append(0.0)
    else:
        temp.append(yval[i])

y_above_x = np.array(temp)

# plotting the 75% babies whose weight is above X
plt.bar(bincentre, y_above_x, width=0.85*binwidth, color='green',
        label = "75% of newborns are born with weight above X")

# plotting x value
plt.plot([x,x],[0.0,max(yval)], c='purple')
text = '''X = {}'''.format(x.astype(float))
plt.text(x=0.87*x, y=0.90*max(yval), s=text, fontsize=10, c='purple')

# display the legend
leg = plt.legend(bbox_to_anchor = (1.01, 0.99), fontsize = 10)
leg.get_frame().set_facecolor('lightgrey')

plt.savefig('newborn_weight_distribution.png')
plt.show()