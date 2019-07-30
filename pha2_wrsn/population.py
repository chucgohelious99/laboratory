# -*- coding: utf-8 -*-
#input:
#hành trình sau khi tìm được ở pha 1
#công suất sạc U
#năng lượng di chuyển của xe E_t
#tổng thời gian sạc của xe to=(E_mc - E_t)/U
#output:
#thời gian sạc cho từng nút dãy các Tou
import random as rd
import individual as indi
class Population:
    def __init__(self,bestWay,nPop,nNode):
#        self.U=U
#        self.E_t=E_t
#        self.E_mc=E_mc
        self.bestWay=bestWay # mảng các Node trong đường đi tốt nhất theo thứ tự
        self.nIndi=len(bestWay)
        self.pop=[]
        self.nNode=nNode
        
        
        
    def run(self,bestWay,to,E_max,E_min,a):
        
        #  khởi tạo
        for i in range(self.nIndi):
            chromosome=[]
            sum_chro=0
            for j in range(self.nNode):
                a= rd.random()
                chromosome.append(a)
                sum_chro+=a
            x=[gen/sum_chro for gen in chromosome]
            newIndi=indi.Individual(x,bestWay,to)
            self.pop.append(newIndi)
            
        #đánh giá cho lần đầu
        for i in range(self.nIndi):
            self.pop[i].calculateFitness(E_max,E_min,a)
        #vòng lặp điều kiện dừng
        for i in range(200):
            population=sorted(self.pop, key= lambda x:x.fitness)
            bestSolution= population[0]
            sum_ele=0
            for element in bestSolution.chromosome:
                sum_ele+= element
#            b= [round(x/sum_ele,4) for x in bestSolution.chromosome ]
#            print(b)
            print(bestSolution.fitness)
            if i ==199:
                new=[round(x*to,2) for x in bestSolution.chromosome]
                print('thời gian sạc cho các nút là')
                print(new)
                print('năng lượng còn lại của các nut')
                bestSolution.printEnergyRemain()
#            if i==99:
#                bestSolution= population[0]
#                sum_ele=0
#                for element in bestSolution.chromosome:
#                    sum_ele+= element
#                b= [round(x/sum_ele,4) for x in bestSolution.chromosome ]
#                print(b)
#                print(bestSolution.fitness)
            # lựa chọn
            s=int((self.nIndi*10)/100)
            new_population=population[:s]
            s=int((self.nIndi*90)/100)
            for j in range(s):
                rand=rd.random()
                if rand>0.5:
                    parent1=rd.choice(population[:50])
                    parent2=rd.choice(population[:50])
                    children=self.crossover(parent1,parent2,to)
                    new_population.append(children)
                elif rand<0.1:
                    parent=rd.choice(population[:50])
                    children=self.mutation(parent,to)
                    new_population.append(children)
                else:
                    chromosome=[]
                    sum_chro=0
                    for j in range(self.nNode):
                        a= rd.random()
                        chromosome.append(a)
                        sum_chro+=a
                    x=[gen/sum_chro for gen in chromosome]
                    child=indi.Individual(x,bestWay,to)
                    new_population.append(child)
                    
            self.pop=new_population
            for k in range(self.nIndi):
                self.pop[k].calculateFitness(E_max,E_min,a)
                
                
            
#-------------------------------------------------------------------            
    def printBestSolution(indiv):
        print(indiv.chromosome)
        
    def crossover(self,parent1,parent2,to):
        ran=rd.randint(1,100)
        childChromosome=[]
        childChromosome.extend(parent1.chromosome[:ran])
        childChromosome.extend(parent2.chromosome[ran:])
        sum_gen=0
        for i in childChromosome:
            sum_gen+=i
        x=[gen/sum_gen for gen in childChromosome]
        child=indi.Individual(x,self.bestWay,to)
        return child
    def mutation(self,parent,to):
        ran=rd.randint(1,99)
        ranVal=rd.random()
        childChromosome=[]
        childChromosome.extend(parent.chromosome)
        childChromosome[ran]=ranVal
        sum_gen=0
        for i in childChromosome:
            sum_gen+=i
        x=[gen/sum_gen for gen in childChromosome]
        child=indi.Individual(x,self.bestWay,to)
        return child
        
            
        
        