# -*- coding: utf-8 -*-
import population as pop
import random as r
import individual as indi


class MultiTasking:
    def __init__(self,tasks,numOfInd,pMutation,timeResetPopulation):
        self.tasks=tasks #  set of tasks namely tsp and solution 2
        self.timeResetPopulation=timeResetPopulation
        self.pMutation=pMutation
        self.population= pop.Population(numOfInd,tasks)
        self.iteration=100
        
    def run(self,nN,set_of_city):
        # initial
        self.population.initial(set_of_city)
        bestSolution=[self.population.individuals[i] for i in range(len(self.tasks))]
        
        #iteration
        changeBest=0
        for i in range(self.iteration):
            for ii in range(len(self.tasks)):
                ind=self.population.getIndividualBestOfTask(ii)
                if bestSolution[ii].fitnessTask[ii] > ind.fitnessTask[ii]:
                    changeBest=0
                    bestSolution[ii]=ind
            changeBest+=1
            if changeBest> self.timeResetPopulation:
                self.population.initial(set_of_city)
                changeBest=0
                
            #crossover and mutation
            individuals=self.population.individuals
            children=[]
            for j in range(nN):
                a=individuals[r.randint(0,len(individuals)-1)]
                b=individuals[r.randint(0,len(individuals)-1)]
                while a==b:
                    b=individuals[r.randint(0,len(individuals))]
                ta=a.skillFactor
                tb=b.skillFactor
                t=r.random()
                
                if ta==tb or t>self.pMutation:
                    children.extend(self.crossOver(a,b))
                else:
                    ia=self.mutation(a)
                    ib=self.mutation(b)
                    children.append(ia)
                    children.append(ib)
            self.reComputeFitnessForChild(children)       
            self.population.individuals.extend(children)
            self.selection()
            self.population.updateRankPopulation()
        bestSolution[0].toString()
      
            #--------------------------------------------------
    def reComputeFitnessForChild(self,children):
        for ind in children:
            fT=ind.fitnessTask
            for j in range(len(self.tasks)):
                if fT[j]==100000000:
                    t=self.tasks[j]
                    fT[j]=t.computeFitness(ind.chromosome)
            ind.fitnessTask=fT
    
    def crossOver(self,a,b):
        children=[]
        factorial_rank=[]
        for i in range(len(self.tasks)):
            factorial_rank.append(self.population.nIndi+1)
        
        child_a=[]
        child_b=[]
        t=r.randint(0,len(a.chromosome))
        
        child_a.extend(a.chromosome[0:t])
        child_b.extend(b.chromosome[0:t])
        for gen in a.chromosome:
            if gen not in child_b:
                child_b.append(gen)
        for gen in b.chromosome:
            if gen not in child_a:
                child_a.append(gen)
                
        ind_a=indi.Individual(child_a,[])
        if r.random()>0.5:
            ind_a.skillFactor=a.skillFactor
        else:
            ind_a.skillFactor=b.skillFactor
        fitnessTa=[0 for x in range(len(self.tasks))]
        for i in range(len(self.tasks)):
            if i!= ind_a.skillFactor:
                fitnessTa[i]=100000000
            else:
                fitnessTa[i]=self.tasks[i].computeFitness(ind_a.chromosome)
        ind_a.fitnessTask=fitnessTa
        ind_a.factorialRank=factorial_rank
        children.append(ind_a)
        
        
        ind_b=indi.Individual(child_b,[])
        if r.random()>0.5:
            ind_b.skillFactor=a.skillFactor
        else:
            ind_b.skillFactor=b.skillFactor
        fitnessTa=[0 for x in range(len(self.tasks))]
        for i in range(len(self.tasks)):
            if i!= ind_b.skillFactor:
                fitnessTa[i]=100000000
            else:
                fitnessTa[i]=self.tasks[i].computeFitness(ind_b.chromosome)
        ind_b.fitnessTask=fitnessTa
        ind_b.factorialRank=factorial_rank
        children.append(ind_b)
        
        return children
    
    def mutation(self,b):
        factorialRank=[0 for x in range(len(self.tasks))]
        for i in range(len(self.tasks)):
            factorialRank.append(self.population.nIndi+1)
        
        t1=r.randint(1,len(b.chromosome)-1)
        t2=r.randint(1,len(b.chromosome)-1)
        child=b.chromosome
        child[t1],child[t2]=child[t2],child[t1]
        
        ind=indi.Individual(child,[])
        ind.skillFactor=b.skillFactor
        fitnessTa=[0 for i in range(len(self.tasks))]
        for i in range(len(self.tasks)):
            if i!= ind.skillFactor:
                fitnessTa[i]=100000000
            else:
                fitnessTa[i]=self.tasks[i].computeFitness(ind.chromosome)
        ind.fitnessTask=fitnessTa
        ind.factorialRank=factorialRank
        
        return ind
        
    def selection(self):
        new_generation=[]
        fitnessTable=[[]for i in range(len(self.tasks))]
        for i in range(len(self.tasks)):
            fitnessTable[i]=sorted(self.population.individuals,key= lambda x:x.fitnessTask[i])
        new_generation.extend(fitnessTable[0][:50])
        while len(new_generation)<=self.population.nIndi:
            for j in fitnessTable[1]:
                if j not in new_generation:
                    new_generation.append(j)
        return new_generation
        
        