"""
Created on date

@author: Nguyễn Văn Chức
"""

class Individual:
    def __init__(self,chromosome,fitness_task):
        self.chromosome=chromosome
        self.fitness_task=fitness_task
        self.factorial_rank=[]
        self.skill_factor=0
        self.scalar_fitness=0
    def getChromosome(self):
        return self.chromosome
    
    def getFitnessTask(self):
        return self.fitness_task
    def setFitnessTask(self,fitnessTask):
        self.fitness_task=fitnessTask
        
    def setFactorialRank(self,factorialRank):
        self.factorial_rank=factorialRank
        
    def getSkillFactor(self):
        return self.skill_factor
    def setSkillFactor(self, skillFactor):
        self.skill_factor=skillFactor
        
    def getScalarFitness(self):
        return self.scalar_fitness
    def setScalarFitness(self,scalarFitness):
        self.scalar_fitness=scalarFitness
    
    def outputForTask(self,task):
        output=[]
        output.append(self.factorial_rank[task])
        output.append(self.fitness_task[task])
        for i in self.chromosome:
            output.append(i)
        return output
    
    