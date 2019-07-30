"""
Created on date

@author: Nguyễn Văn Chức
"""

class Task:
    def __init__(self,graph):
        """ graph là một mảng hai chiều chứa danh sách kề """
        self.graph=graph
        self.dimension=len(self.graph)
        
    def decode(self,chromosome):
        kq=[]
        index=0
        for i in chromosome:
            if i< self.dimension:
                kq.append(i)
        return kq
    
    def computeFitness(self, chromosome):
        temp=self.decode(chromosome)
        length=len(temp)
        fitness=self.graph[temp[0]][temp[length-1]]
        for i in range(length):
            fitness+= self.graph[temp[i]][temp[i+1]]
        return fitness