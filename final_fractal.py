#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:28:57 2020

@author: malika
"""


import turtle

def get_sierpinski(length,level):
    
    turtle.speed(100)
    
    if level == 1:             #base case
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
            
    else:
        get_sierpinski(length/2, level-1)      #recursive case which divides the problem into 3 equal parts
        
        turtle.forward(length/2)
        
        get_sierpinski(length/2, level-1)
        
        turtle.back(length/2)
        
        turtle.left(60)
        
        turtle.forward(length/2)
        
        turtle.right(60)
        
        get_sierpinski(length/2, level-1)
        
        turtle.left(60)
        
        turtle.back(length/2)
        
        turtle.right(60)

length = int(input("Enter the base length of the triangle : "))  #User can include the depth of the triangle

level = int(input("Enter the depth of the triangle : "))      #User can input the depth of recursion

get_sierpinski(length,level)

turtle.getscreen().getcanvas().postscript(file='3dprint.ps')  #format referred from stack overflow

        
        