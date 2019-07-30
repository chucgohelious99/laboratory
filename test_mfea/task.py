"""
Created on date

@author: Nguyễn Văn Chức
"""

class Task:
    def __init__(self,dimension):
        self.dimension=dimension
    
    def decode(self,individual):
        x=[]
        for i in individual.chromosome:
            if i.number<self.dimension:
                x.append(i)
        return x
# x la một tập các gen 
# dưới đây là hàm tính độ thích nghi với task
    def fitness(self,individual):
        x=self.decode(individual)
        lengx=len(x)
        fitness=x[0].distanceto(x[lengx-1])
        for i in range(lengx-1):
            fitness+= x[i].distanceto(x[i+1])
        return fitness
    def populationFitness(self,population):
        x=[]
        for i in population.pop:
            x.append(self.fitness(i))
        return x
    