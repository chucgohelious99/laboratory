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
        
    def initial(self, set_of_city):
        individuals=[]
        
        for i in range(self.nIndi):
           new_chromosome=r.sample(set_of_city,self.lenGen)
           fitnessTa=[]
           for task in self.tasks:
               fitnessTa.append(task.computeFitness(new_chromosome))
           new_indi=indiv.Individual(new_chromosome,fitnessTa)
           
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
    
    def add(self,offsprings):
        
        for index in range(len(offsprings)):
            child= offsprings[index]
            child_task=child.skillFactor
            
            rankInTask=self.countRank(child_task)
            indexx=-1
            for j in range(len(rankInTask)):
                if rankInTask[j].fitnessTask[child_task]>child.fitnessTask[child_task]:
                    indexx=j
                    break
                
            if indexx>-1:
                for j in range(indexx,len(rankInTask)):
                    tmp=rankInTask[j]
                    rank=tmp.factorialRank
                    rank[child_task]+=1
                    tmp.factorialRank=rank
                    rankInTask[j]=tmp
            else:
                indexx=len(rankInTask)
                
            facRankInd=[]
            for ii in range(self.nTask):
                facRankInd.append(len(self.individuals)+1)
            facRankInd[child_task]=indexx+1
            child.factorialRank=facRankInd
            offsprings[index]=child
        
        for ind in offsprings:
             ind.scalarFitness=1.0/ind.getMinFactorialRank()
        
        self.individuals.extend(offsprings)          
                
            #______________________________________________________
    def countRank(self,task):
        lstIndividualInTask=[]
        for i_in in range(self.nIndi):
            ind=self.individuals[i_in]
            for i in range(self.nTask):
                check=True
                for j in range(len(lstIndividualInTask)):
                    if lstIndividualInTask[j].fitnessTask[i] > ind.fitnessTask[i]:
                        lstIndividualInTask.insert(ind,j)
                        check=False
                        break
                if check:
                    lstIndividualInTask.append(ind)
        return lstIndividualInTask
    
    def getIndividualBestOfTask(self,task_in_num):
        for indi in self.individuals:
            if indi.factorialRank[task_in_num]==1:
                best=indi
                return best
        
