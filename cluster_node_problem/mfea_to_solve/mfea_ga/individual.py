# -*- coding: utf-8 -*-
class Individual:
    def __init__(self,chromosome,fitnessTask):
        self.chromosome=chromosome #chromosome is an array of integer
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
    
    def convertToNode(self,set_of_node,pole,v,p_m,e_m):
        tm=sorted(self.chromosome)
        result=[]
        for i in self.chromosome:
            result.append(tm.index(i))
        node_chro=[]
        for index in result:
            for node in set_of_node:
                if node.number==index:
                    node_chro.append(node)
        longestWay=e_m*v/p_m
        sumLengWay=0
        lengWay=node_chro[0].distanceTo(pole)
        new_node_chro=[]
        last=len(node_chro)-1
        for i in range(len(node_chro)-1):
            new_node_chro.append(node_chro[i])
            lengWay +=node_chro[i].distanceTo(pole)
            if lengWay> longestWay:
                new_node_chro.append(pole)
                sumLengWay+=lengWay
                lengWay= node_chro[i+1].distanceTo(pole)
        new_node_chro.append(node_chro[last])
        lengWay+= node_chro[last].distanceTo(pole)
        sumLengWay+=lengWay
        return new_node_chro
    
    def toString(self,set_of_node,pole,v,p_m,e_m):
        result_string=[i.number for i in self.convertToNode(set_of_node,pole,v,p_m,e_m)]
        return result_string
