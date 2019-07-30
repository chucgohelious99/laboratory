# -*- coding: utf-8 -*-
import random as r


class Population:
    def __init__(self,nIndividual,tasks):
        self.nIndividual=nIndividual
        self.nTask=len(tasks)
        self.tasks=tasks
        self.individuals=[]
        max_in=0
        for task in self.tasks:
            if task.getLenGen()>max_in:
                max_in=task.getLenGen()
        self.lenGen=max_in
        
    def initial(self):
        for i in range(self.nIndividual):
            g=[r.random() for j in range(self.lenGen)]
            if(check)
            
    
    #---------------------------------------------------------
    def checkIndividualVail(self,ind):
        for t in self.tasks:
            if t.checkIndividualVail(ind):
                return True
        return False
    
    def makeIndividualVail(self,ind)
        i=0
        xd=0
        while True:
            if self.tasks[i].checkIndividualVail(ind):
                xd=0
                self.tasks[i].makeIndividualVail(ind)
            else:
                xd+=1
            if xd>= self.nTask:
                break
            
            i=(i+1)% self.nTask
    def updateRankPopulation(self):
        rankInTask=[[] for i in range(self.nTask)]
        for i_in in range(self.nIndividual):
            ind=self.individuals[i_in]
            for i in range(self.nTask):
                lstIndividualInTask = rankInTask[i]
                check=True
                for j in range(len(lstIndividualInTask)):
                    if lstIndividualInTask[j].fitnessTask[i] > ind.fitnesstask[i]
                
                
                
                
                
                