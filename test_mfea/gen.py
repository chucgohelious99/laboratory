"""
Created on date

@author: Nguyễn Văn Chức
"""
import math
class Gen:
    def __init__(self,number,x,y):
        self.x=x
        self.y=y
        self.number= number
    def print_coordinate(self):
        print('(',self.x,',',self.y,')')
    def distanceto(self,other):
        distanceX=self.x-other.x
        distanceY=self.y-other.y
        return math.sqrt(distanceX**2+distanceY**2)