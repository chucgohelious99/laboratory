# -*- coding: utf-8 -*-
class Task:
    def __init__(self,dimension):
        self.dimension=dimension
        
    def getStride(self,tx,tmp_tx,window):
        stride=0
        if (len(tmp_tx)-len(window))%(self.dimension-1)==0:
            stride=(len(tmp_tx)-len(window))/(self.dimension-1)
        else:
            stride=(len(tmp_tx)-len(window))/(self.dimension-1) +1
            zero_padding= (self.dimension-1)*stride + len(window)-len(tx)
            for i in range(zero_padding):
                tmp_tx.append(0)
        return stride
    
