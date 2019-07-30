# -*- coding: utf-8 -*-
#we consider individual as a list of float number between 0 and 1
#than decode them by sorting them and save their position in order 
#list to associative position in chromosome

class Individual:
    def __init__(self,chromosome,fitness):
        self.chromosome=chromosome
        self.fitness=fitness
        
    def decode(self):
        tm=sorted(self.chromosome)
        result=[]
        for i in self.chromosome:
            result.append(tm.index(i))
        return result
    
    def computeFitness(self,set_of_node,pole,v,p_m,e_m,U):
        #set_of_node is an array of node
        chro_decode=self.decode()
        node_chro=[]
        for index in chro_decode:
            for node in set_of_node:
                if node.number==index:
                    node_chro.append(node)
        #computing time for cycle
        T=0
        for node in set_of_node:
            node.computeTLife()
            if node.t_life>T:
                T=node.t_life
                
        #inject Pole node to chromosome
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
        sumLengWay+=lengWay # sumLengWay contains leng of whole cycle includes times which come back depot
        t_tsp=sumLengWay/v
        #computing waiting time
        t_charge=[]
        lengWait=new_node_chro[0]. distanceTo(pole)
        for i in range(len(new_node_chro)-1):
            time_x=lengWait*new_node_chro[i].p/(v*(U-new_node_chro[i].p))
            t_charge.append(time_x)
            lengWait += new_node_chro[i].distanceTo(new_node_chro[i+1])
        time_x_last=lengWait*new_node_chro[len(new_node_chro)-1].p/(v*(U- new_node_chro[len(new_node_chro)-1].p))
        t_charge.append(time_x_last)
        sum_t_charg=0
        for time in t_charge:
            sum_t_charg+= time
        #computing vacation time
        t_vac=T - t_tsp - sum_t_charg
        #computing fitness
        self.fitness=t_vac/T
    
    def toString(self,set_of_node,pole,v,p_m,e_m):
        chro_decode=self.decode()
        node_chro=[]
        for index in chro_decode:
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
        
        a=[node.number for node in new_node_chro]
        print(a)
            
            
            
            
            
                
                
            
        
        
        
        
        