# -*- coding: utf-8 -*-
import individual as indiv
import random as r
# individual includes chromosome which is seen as set of real number within 0 and 1 

class Population:
    def __init__(self,nIndi,set_of_node):
        self.nIndi=nIndi
        self.individuals=[]
        self.dimension=len(set_of_node)
        
    def initial(self,set_of_node,pole,v,p_m,e_m,U):
        individuals_x=[]
        for i in self.nIndi:
            chromosome=[r.random()  for j in range(self.dimension)]
            new_indi=indiv.Individual(chromosome,0)
            new_indi.computeFitness(set_of_node,pole,v,p_m,e_m,U)
            individuals_x.append(new_indi)
        self.individuals=individuals_x
    def generateChildren(self):
        new_individual=sorted(self.individuals,key= lambda x:x.fitness)
        new_individual.reverse()
        
        children=[]
        for i in range(int(self.nIndi/2)):
            t=r.random()
            p_mutation=0.08
            if t<p_mutation:
                par=new_individual[r.randint(0,self.dimension)]
                children.append(self.mutation(par))
            else:
                par1=new_individual[r.randint(50,self.dimension)]
                par2=new_individual[r.randint(50,self.dimension)]
                children.append(self.crossover(par1,par2))
        return children
    
    def selection(self,children):
        newGeneration=self.individuals
        newGeneration.extend(children)
        newGeneration=sorted(newGeneration,key= lambda x:x.fitness)
        newGeneration.reverse()
        self.individuals=newGeneration[:self.nIndi]
        
        
                #-------------------------------------
    def mutation(self,parent):
        chro=parent.chromosome
        t_x1=int(r.random()*self.dimension)
        t_x2=int(r.random()*self.dimension)
        chro[t_x1],chro[t_x2]=chro[t_x2],chro[t_x1]
        child= indiv.Individual(chro,0)
        child.computeFitness()
        return child
    
    def crossover(self,par1,par2):
        chro_child=[]
        t_x=int(r.random()*self.dimension)
        chro_child.extend(par1.chromosome[:t_x])
        chro_child.extend(par2.chromosome[t_x:])
        child=indiv.Individual(chro_child,0)
        child.computeFitness()
        return child
    
    def printBestIndi(self,set_of_node,pole,v,p_m,e_m):
        hehe=sorted(self.individuals,key= lambda x:x.fitness)
        hehe.reverse()
        hehe[0].toString(set_of_node,pole,v,p_m,e_m)
        
