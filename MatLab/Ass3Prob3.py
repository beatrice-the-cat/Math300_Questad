# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:39:05 2022

Evan Questad
Assignment 3
Problem 3
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def problem3(N, x):
    list = []
    sum = 0
    for i in range(N):
        n = i + 1
        sum += (x**n) / (n)
        list.append(sum)
    plt.title("Problem 3 Plot")
    plt.plot(list)
    plt.show()
    return sum
        
print(problem3(8, 4))