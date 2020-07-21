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
        get_sierpinski(length/2, level-1)
        
        turtle.forward(length/2)
        
        get_sierpinski(length/2, level-1)
        
        turtle.back(length/2)
        
        turtle.left(60)
        
        turtle.forward(length/2)
        
        