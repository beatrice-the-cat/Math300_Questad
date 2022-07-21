# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:39:31 2022

Evan Questad
Assignment 3
Problem 5
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as s



x = s.symbols('x')
d = s.diff(((x**3) - ((s.cos(x*np.pi))/(2*x**2 + 1)) + ((11/3*x**2)) - (1)), x)
return d
