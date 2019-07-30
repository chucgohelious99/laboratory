# -*- coding: utf-8 -*-
import ga.task
import random as r
class TSP(ga.task.Task):
    def __init__(self,graph,dimension):
        self.graph=graph # mảng hai chiều chứa dữ liệu đầu vào
        ga.task.Task.__init__(self,dimension)
    
    def decode(self,tx):
        x=[]
        tmp_tx=tx
        if len(tmp_tx)>self.dimension:
            window=[r.random(),r.random()]
            stride=self.getStride(tx,tmp_tx,window)
            for i in range(0,len(tmp_tx),stride):
                tmp_x=0
                for j in range(len(window)):
                    tmp_x +=tmp_tx[i+j].window[j]
                    x.extend(tmp_x)
        else:
            x=tmp_tx
            # mai viết tiếp
            
