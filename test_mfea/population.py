"""
Created on date

@author: Nguyễn Văn Chức
"""
import random as r
import individual as idv

class Population:
    def __init__(self,nIndividual,listTask):
        self.nIndividual=nIndividual
        self.listTask=listTask # danh sách các Task
        self.nTask=len(listTask)
        self.pop=[] #mảng chứa các individual
        maxdi=listTask[0].dimension
        for i in listTask:
            if i.dimension>maxdi:
                maxdi=i.dimension
        self.pop_dimension=maxdi
        
    def init_pop(self, set_of_city):#set of city là tập các thành phố có thể làm gen
        for i in range(self.nIndividual):   
            set_of_gens=r.sample(set_of_city,self.pop_dimension)
            indi=idv.Individual(set_of_gens, self.nTask)
            a=[]
            for j in self.listTask:
                a.append(j.fitness(indi))
            indi.setFactorialCost(a)
            self.pop.append(indi)
            
    def update_rank(self):
        rankInTask=[[] for j in range(self.nTask)]
        #update lại rank trên từng task, nếu còn trống thì nạp indi vào
        for i_in in range(self.nIndividual):
            ind=self.pop[i_in]
            for i in range(self.nTask):
                listIndiInTask=rankInTask[i]
                check=True
                for j in range(len(listIndiInTask)):
                    if listIndiInTask[j].factorial_cost[i]>ind.factorial_cost[i]:
                        listIndiInTask.insert(j,ind)
                        check=False
                        break
                if check:
                    listIndiInTask.append(ind)
                rankInTask[i]=listIndiInTask
        for i in range(self.nIndividual):
            ind=self.pop[i]
            factorialRank=[0]*self.nTask
            min_rank=self.nIndividual+2
            task_rank_min=-1
            for j in range(self.nTask):
                rankJ=rankInTask[j].index(ind)+1
                factorialRank[j]=rankJ
                if rankJ<min_rank:
                    min_rank=rankJ
                    task_rank_min=j
            ind.setFactorialRank(factorialRank)
            ind.setSkillFactor(task_rank_min)
            for x in range(self.nTask):
                if x!=ind.skill_factor:
                    ind.factorial_cost[x]=100000
            ind.setScalarFitness(float(1/min_rank))
    
    def addOffSpring(self,offsprings):
        self.pop.extend(offsprings)
        
        for i in range(len(self.pop)):
            child=self.pop[i]
            child_task=child.skill_factor
            factorialRank=[0 for j in range(self.nTask)]
            for x in range(len(factorialRank)):
                factorialRank=len(self.pop)+1
            rankInTask=self.countRank(child_task)
            for j in range(len(rankInTask)):
                if child==rankInTask[j]:
                    factorialRank[child_task]=j+1
                    child.setScalarFitness(float(1.0/factorialRank[child_task]))
            child.setFactorialRank(factorialRank)
            
    
    def countRank(self,task):
        listIndiInTask=[]
        for indi in self.pop:
            check=True
            for j in range(len(listIndiInTask)):
                if listIndiInTask[j].factiorial_cost[task]>indi.factorial_cost[task]:
                    listIndiInTask[j]=indi
                    check=False
                    break
            if check:
                listIndiInTask.append(indi)
        return listIndiInTask
    
    def getBestIndiOfTask(self,task):
        best=None
        for indi in self.pop:
            if indi.factorial_rank[task]==1:
                best=indi
        return best