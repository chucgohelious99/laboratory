# -*- coding: utf-8 -*-
class Individual:
    def __init__(self,chromosome,bestWay,to):
        self.chromosome=chromosome # mảng các thười gian sạc cho các node
        self.bestWay=bestWay
        self.to=to
        self.fitness=0
    def calculateFitness(self,E_max,E_min,a): #a là chiều dài lớn nhất
        sum_gen=0
        for i in self.chromosome:
            sum_gen+=i
        textChromosome=[x/sum_gen for x in self.chromosome]
        self.chromosome=textChromosome
        fitness=0
        lengWay=self.bestWay[0].distanceToPole()
        charTimeBefore=0# thòi gian đến nút đó sạc
        charTimeAfter=0# thời gian sạc nút vừa xong
        E_cur1=self.bestWay[0].E_start-(charTimeBefore+lengWay/5)*self.bestWay[0].performance+(5-self.bestWay[0].performance)*self.chromosome[0]*self.to
        if(E_cur1>E_max):
            E_cur1=E_max
        if self.bestWay[0].E_start-(charTimeBefore+lengWay/5)*self.bestWay[0].performance < E_min:
            fitness+=1
            charTimeAfter= charTimeBefore#chết ko sạc cho nữa
            self.chromosome[0]=0
            self.bestWay[0].setEnergyRemain(E_min)
        elif E_cur1-((a-lengWay)/5 +self.to-charTimeAfter)*self.bestWay[0].performance <E_min:
            fitness +=1
            charTimeAfter+=self.chromosome[0]*self.to 
            self.bestWay[0].setEnergyRemain(E_min)
        else:
            m= E_cur1-((a-lengWay)/5 +self.to-charTimeAfter)*self.bestWay[0].performance
            self.bestWay[0].setEnergyRemain(m)
            charTimeAfter+=self.chromosome[0]*self.to 
        charTimeBefore= charTimeAfter 
        for i in range(1,len(self.bestWay)):
            lengWay+= self.bestWay[i-1].distanceTo(self.bestWay[i])
            E_cur=self.bestWay[i].E_start-(charTimeBefore+lengWay/5)*self.bestWay[i].performance+(5-self.bestWay[0].performance)*self.chromosome[i]*self.to
            if(E_cur>E_max):
                E_cur=E_max
           
            if self.bestWay[i].E_start-(charTimeBefore+lengWay/5)*self.bestWay[i].performance <E_min:
                fitness+=1
                charTimeAfter=charTimeBefore
                self.chromosome[i]=0
                self.bestWay[i].setEnergyRemain(E_min)
            elif E_cur-((a-lengWay)/5+self.to-charTimeAfter)*self.bestWay[i].performance <self.bestWay[i].E_start:
                fitness+=1
                self.bestWay[i].setEnergyRemain(E_min)
                charTimeAfter+=self.chromosome[i]*self.to
            else:
                m= E_cur-(a/5-lengWay/5 +self.to-charTimeAfter)*self.bestWay[i].performance
                self.bestWay[i].setEnergyRemain(m)
                charTimeAfter+=self.chromosome[i]*self.to
            charTimeBefore=charTimeAfter
        self.fitness=fitness
    def printEnergyRemain(self):
        energyRemain=[i.E_remain for i in self.bestWay]
        print(energyRemain)
        

