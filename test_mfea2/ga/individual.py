# -*- coding: utf-8 -*-

class Individual:
    def __init__(self,gen,fitnessTask):
        self.gen=gen # gen là chuổi gen của cá thể
        self.fitnessTask= fitnessTask #là mảng các fitness đối vưới các task
        self.factorial_rank=[]
        self.skillFactor=0
        self.scalarFitness=0
    
    def getMinFactorialRank(self):
        int_min=10000000
        for tmp in self.factorial_rank:
            if int_min >tmp:
                int_min=tmp
        return int_min
    
    def getGen(self):
        return self.gen
    
    def getFitnessTask(self):
        return self.fitnessTask
    
    def getSkillFactor(self):
        return self.skillFactor
    def setSkillFactor(self,skillFactor):
        self.skillFactor=skillFactor
    
    def getScalarFitness(self):
        return self.scalarFitness
    def setScalarFitness(self,scalarFitness):
        self.scalarFitness=scalarFitness
        
    def getFactorialRank(self):
        return self.factorial_rank
    def setFactorialRank(self,factorialRank):
        self.factorial_rank=factorialRank
        
    def toString():
        print('đề nghị đồng chí tự viết tiếp đoạn này')