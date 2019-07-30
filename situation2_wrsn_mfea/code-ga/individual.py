# -*- coding: utf-8 -*-
class Individual:
    def __init__(self,chromosome,fitnessTask):
        self.chromosome=chromosome #chroosome includes depot as 0
        self.fitnessTask= fitnessTask
        self.factorialRank=[]
        self.skillFactor=0
        self.scalarFitness=0
        
    def getMinFactorialRank(self):
        min_int=10000000
        for rank in self.factorialRank:
            if min_int >rank:
                min_int =rank
        return min_int
    
    def setFitnessTask(self,fitnessTask):
        self.fitnessTask=fitnessTask
        
    def setSkillFactor(self,skillFactor):
        self.skillFactor=skillFactor
        
    def setScalarFitness(self,scalarFitness):
        self.scalarFitness=scalarFitness
        
    def setFactorialRank(self,factorialRank):
        self.factorialRank=factorialRank
    
    def toString(self):
        print([i.number for i in self.chromosome])