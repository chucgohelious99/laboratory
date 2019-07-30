# -*- coding: utf-8 -*-
import individual as indiv
import random as r

class Population:
    def __init__(self,nIndi,tasks):
        self.nIndi=nIndi
        self.tasks=tasks
        self.nTask=len(tasks)
        self.individuals=[]
        max_dimension=0
        for task in tasks:
            if task.dimension > max_dimension:
                max_dimension= task.dimension
        self.lenGen=max_dimension
        
    def initial(self):
        individuals=[]
        
        for i in range(self.nIndi):
           new_chromosome=[r.random() for i in range(self.lenGen)]
           new_indi=indiv.Individual(new_chromosome,[])
           fitnessTa=[]
           for task in self.tasks:
               fitnessTa.append(task.computeFitness(new_indi))
           new_indi.fitnessTask=fitnessTa
           individuals.append(new_indi)
        self.individuals=individuals
        self.updateRankPopulation()
        
        
        
    def updateRankPopulation(self):
        rankInTask=[[] for i in range(self.nTask)]
         
        for i_in in range(self.nIndi):
            ind=self.individuals[i_in]
            for i in range(self.nTask):
                lstIndividualInTask=rankInTask[i]
                check=True
                for j in range(len(lstIndividualInTask)):
                    if lstIndividualInTask[j].fitnessTask[i] > ind.fitnessTask[i]:
                        lstIndividualInTask.insert(j,ind)
                        check=False
                        break
                if check:
                    lstIndividualInTask.append(ind)
                
                rankInTask[i]=lstIndividualInTask
                
        for i in range(self.nIndi):
            indx=self.individuals[i]
            factorial_Rank=[]
            min_rank=self.nIndi+2
            task_rank_min=-1
            
            for j in range(self.nTask):
                rankJ= rankInTask[j].index(indx)+1
                factorial_Rank.append(rankJ)
                if rankJ<min_rank:
                    min_rank=rankJ
                    task_rank_min=j
                    
            indx.factorialRank=factorial_Rank
            indx.skillFactor=task_rank_min
            indx.scalarFitness=(1.0/min_rank)
