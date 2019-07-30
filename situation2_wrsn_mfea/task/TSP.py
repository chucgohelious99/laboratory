# -*- coding: utf-8 -*-

class TSP:
    def __init__(self,dimension,set_of_gen):
        self.dimension=dimension
        self.set_of_gen=set_of_gen
        
    def decode(self,chromosome): #individual is set of Node in order
        result_decode=[]
        for gen in chromosome:
            if gen.number <= self.dimension and gen.number != 0:
                result_decode.append(gen)
        return result_decode
    def computeFitness(self,chromosome):
        result_decode=self.decode(chromosome)
        last_index=len(result_decode)-1
        fitness= result_decode[0].distanceToPole() + result_decode[last_index].distanceToPole()
        for i in range(last_index):
            fitness += result_decode[i].distanceTo(result_decode[i+1])
        return fitness
    