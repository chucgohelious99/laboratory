"""
Created on date

@author: Nguyễn Văn Chức
"""
import math
class gen:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self,other_gen):
        distance_x=self.x - other_gen.x
        distance_y=self.y - other_gen.y
        distance= math.sqrt(distance_x**2+distance_y**2)
        return distance