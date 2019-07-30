# -*- coding: utf-8 -*-

class Task:
    def __init__(self,dimension):
        self.dimension=dimension
        self.e_max=10800
        self.e_min=540
        self.U=5
        self.v=5
        self.e_m=4000
        self.p_m=1
    
    def decode(self,indi,set_of_node,pole):
        tm=sorted(indi.chromosome)
        result=[]
        for i in indi.chromosome:
            if i<=self.dimension:    
                result.append(tm.index(i))
        return result # hàm trả về đã bao gồm nút 0
    def computeFitness(self,indi,set_of_node,pole):
        chro_decode=self.decode()
        node_chro=[]
        for index in chro_decode:
            for node in set_of_node:
                if node.number==index:
                    node_chro.append(node)
        T=0
        for node in set_of_node:
            node.computeTLife()
            if node.t_life>T:
                T=node.t_life      
        #inject Pole node to chromosome
        longestWay=self.e_m*self.v/self.p_m
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
        t_tsp=sumLengWay/self.v
        #computing waiting time
        t_charge=[]
        lengWait=new_node_chro[0]. distanceTo(pole)
        for i in range(len(new_node_chro)-1):
            time_x=lengWait*new_node_chro[i].p/(self.v*(self.U-new_node_chro[i].p))
            t_charge.append(time_x)
            lengWait += new_node_chro[i].distanceTo(new_node_chro[i+1])
        time_x_last=lengWait*new_node_chro[len(new_node_chro)-1].p/(self.v*(self.U- new_node_chro[len(new_node_chro)-1].p))
        t_charge.append(time_x_last)
        sum_t_charg=0
        for time in t_charge:
            sum_t_charg+= time
        #computing vacation time
        t_vac=T - t_tsp - sum_t_charg
        #computing fitness
        fitness=t_vac/T
        return fitness
        #sửa lại, chuyển hàm to string từ individual sang đây
        