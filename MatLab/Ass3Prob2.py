# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:37:34 2022

Evan Questad
Assignment 3
Problem 2
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def problem2(N):
    list = []
    sum = 0
    for i in range(N):
        n = i + 1
        sum += ((-1)**(n+1)) * (1/n)
        list.append(sum)
    v = np.array(list)
    plt.plot(v)      
    plt.title('Problem 2 Plot')  
    plt.show()
    return sum



    
print(problem2(50))



        