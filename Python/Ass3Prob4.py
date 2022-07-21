# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:39:20 2022

Evan Questad
Assignment 3
Problem 4
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def midpoint(f, a, b, N):
    
    #the space between each point, required to use np.arange
    n = (b-a)/N
    #x is now a list of all the divided points, from 0 to N-1
    x = np.arange(a, b+n, n)
    #variable for adding our values up
    sum = 0
    #plotting stuff
    plt.plot(x, f(x), color='black')
    y = np.arange(a, b, n)
    plt.bar(y, f(y), color='orange', edgecolor='blue', width=n, alpha=0.5)
    #for loop runs once for each partition
    for i in range(N):
        #if statement to catch out of bounds
        if i == (N-1):
            sum += f( (x[i] + b) /2 ) * (b-x[i])
            continue
        #uses midpoint for the function call, multiplied by distance between the points
        sum += f( (x[i] + x[i+1]) /2 ) * (x[i+1]-x[i])
        
    #returns the sum when finished
    return sum

#function for testing
def f(x):
    return x**2 + x

#testing
print(midpoint(f, 1, 10, 50))
