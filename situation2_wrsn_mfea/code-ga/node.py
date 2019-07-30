# -*- coding: utf-8 -*-
import math as m

class Node:
    def __init__(self,number,x,y,performance,e_start):
        self.number=number
        self.x=x
        self.y=y
        self.p=performance
        self.e_start=e_start
        
        e_max=10800
        e_min=540
        U=5
        self.t_life=(e_max-e_min)/(U-self.p) + (e_max-e_min)/self.p
        
    
    def distanceTo(self,other_node):
        disX=self.x-other_node.x
        disY=self.y-other_node.y
        return m.sqrt(disX**2+disY**2)
    
    def distanceToPole(self):
        return m.sqrt(self.x**2+self.y**2)
    
    
    
