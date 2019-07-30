# -*- coding: utf-8 -*-

class Situation2:
    def __init__(self,dimension):
        self.e_max=10800
        self.e_min=540
        self.U=5
        self.v=5
        self.e_m=4000
        self.dimension=dimension
        
    def computeFitness(self,route):
        # compute cycle time
        T=0
        for node in route:
            if node.t_life > T:
                T=node.t_life
        #compute time for transport in hamilton loop
        last=len(route)-1
        lengWay= route[0].distanceToPole()+route[last].distanceToPole()
        for i in range(last):
            lengWay += route[i].distanceTo(route[i+1])
        t_tsp= lengWay/self.v
        #compute time for charging in each node
        t_charg=[]
        lengWait=route[0].distanceToPole()
        for i in range(last):
            time_x=lengWait*route[i].p/(self.v*(self.U-route[i].p))
            t_charg.append(time_x)
            lengWait += route[i].distanceTo(route[i+1])
        time_x_last=lengWait*route[last].p/(self.v*(self.U-route[last].p))
        t_charg.append(time_x_last)
        sum_t_charg=0
        for time in t_charg:
            sum_t_charg+= time
        # compute vacation time in depot
        t_vac= T - t_tsp - sum_t_charg
        ratio_time= t_vac/T
        return ratio_time