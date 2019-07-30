# -*- coding: utf-8 -*-
import math as m
class Node:
    def __init__(self,number,x,y,performance,E_start,E_max,E_min,U):
        self.x=x
        self.y=y
        self.number=number
        self.E_start=E_start
        self.status=0 # mặc định ban đầulà cho node sống
        self.performance=performance
        self.maxT=(E_max - E_min)/(U-self.performance)+(E_max - E_min)/self.performance
        self.E_remain=0
        
#    def getX(self):
#        return self.x
#    def getY(self):
#        return self.y
    def setStatus(self,status):
        self.status=status
    def getStatus(self):
        return self.status
    def distanceTo(self,other_node):
        disX=self.x-other_node.x
        disY=self.y-other_node.y
        return m.sqrt(disX**2+disY**2)
    def distanceToPole(self):
        return m.sqrt(self.x**2+self.y**2)
    def setEnergyRemain(self,energy):
        self.E_remain=energy
    
