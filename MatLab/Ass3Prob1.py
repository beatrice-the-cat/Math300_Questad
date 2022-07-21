# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:07:46 2022

Evan Questad
Assignment 3
Problem 1
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([5, 8])
x = np.linalg.solve(a, b)
print(x)