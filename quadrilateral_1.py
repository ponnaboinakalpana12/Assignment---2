# -*- coding: utf-8 -*-
"""Quadrilateral:1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/118lh9SdzlPQ5gfgEoCPbDnX6hgQEmDYc
"""

import matplotlib.pyplot as plt
 
M, I, S, T = (0, 0), (3.5, 0), (5.18,6.27), (2.42, 9.03)
 
 
def line_gen(C1, C2):
    return ((C1[0], C2[0]), (C1[1], C2[1]))
 
 
l1 = line_gen(M, I)
l2 = line_gen(I, S)
l3 = line_gen(S, T)
l4 = line_gen(T, M)
l5 = line_gen(S, M)
 
 
def drawLine(line):
    plt.plot(line[0], line[1])
    
def drawVertix(coordinate, name):
    plt.plot(coordinate[0], coordinate[1], 'o')
    plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)
 
 
# drawing Quadrilateral
drawLine(l1)
drawLine(l2)
drawLine(l3)
drawLine(l4)
drawLine(l5)
 
# plotting vertices
drawVertix(M, "M")
drawVertix(I, "I")
drawVertix(S, "S")
drawVertix(T,"T") 
 
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Quadrilateral MIST')
plt.grid()
plt.show()
