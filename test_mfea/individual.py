"""
Created on date

@author: Nguyễn Văn Chức
"""

class Individual:
    def __init__(self,set_of_gens,nTask):
        self.chromosome=set_of_gens
        self.nGens=len(set_of_gens)
        self.factorial_cost=[0 for i in range(nTask)]
        self.factorial_rank=[0 for i in range(nTask)]
        self.scalar_fitness= None
        self.skill_factor=None
        
    def getChroomosome(self):
        return self.chromosome
    def setChromosome(self,set_of_gens):
        self.chromosome=set_of_gens
    def setFactorialCost(self,array_of_fitness):
        self.factorial_cost=array_of_fitness
    def setFactorialRank(self,array_of_rank):
        self.factorial_rank=array_of_rank
    def setSkillFactor(self,skill_factor):
        self.skill_factor=skill_factor
    def setScalarFitness(self,scalar_fitness):
        self.scalar_fitness=scalar_fitness
        