"""
Created on date

@author: Nguyễn Văn Chức
"""
import random as r
import tspTask as tt
import individual as indi
class Population:
    def __init__(self, nPop,listTask):
        self.nIndividual=nPop
        self.tasks=listTask
        self.nTasks=len(listTask)
        self.individual=[]
        self.dimension= max(listTask)
        
    def initpop(self):
        for t in range(self.nIndividual): 
            gen=[]
            for i in range(self.dimension):
                gen.append(i)
            for i in range(self.dimension):
                k=r.randint(0,j)
                gen[k],gen[j]=gen[j],gen[k]
            fitness=[]
            for i in range(self.nTasks):
                fitness.append(self.tasks[i].computeFitness(gen))
            ind=indi.Individual(gen,fitness)
            self.individual.append(ind)
        self.updateRank()
    
    def updateRank(self):
        rankInTask=[[] for i in range(self.nTasks)]
        for i in range(self.nIndividual):
            ind=self.individual[i]
            a=ind.getFitness
            for j in range(self.nTasks):
                oneInTask=rankInTask[j]
                check= True
                for x in len(oneInTask):
                    if oneInTask[x]>a[x]:
                        oneInTask[x]=a[x]
                        check=False
                        break
                if check:
                    oneInTask.append(ind)
            rankInTask[j]=oneInTask
            
        for i in range(self.nIndividual):
            ind=self.individual[i]
            factorial_rank=[0 for k in range(self.nTasks)]
            min_rank=self.nIndividual+2
            task_rank_min=-1
            for j in range(self.nTasks):
                rankJ=rankInTask[j].index(ind)+1
                
                
        
                
            
        