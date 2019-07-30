"""
Created on date

@author: Nguyễn Văn Chức
"""
import population as pp
import random as r
import individual as idv
import task 
import gen
class MultiTasking:
    def __init__(self,listTask, nInd,pMutation, set_of_city):
        self.set_of_city=set_of_city
        self.listTask=listTask
        self.nInd=nInd
        self.population=pp.Population(nInd,listTask)
        self.pMutation=pMutation
        self.iteration=0
        self.crossover=0
        self.mutation=0
        for i in listTask:
            maxdi=listTask[0].dimension
            if i.dimension>maxdi:
                maxdi=i.dimension
        self.pop_dimension=maxdi
        
    def Crossover(self,parent1,parent2):
        childList=[]
        a=r.randint(0,self.pop_dimension)
        gen_child1=parent1.chromosome[:a]
        gen_child1.extend(parent2.chromosome[a:])
        gen_child2=parent2.chromosome[:a]
        gen_child2.extend(parent1.chromosome[a:])
        child1=idv.Individual(gen_child1,len(self.listTask))
        child2=idv.Individual(gen_child2,len(self.listTask))
        # phân vân giữa chọn hay không chọn các yếu tố
        childList.append(child1)
        childList.append(child2)
        return childList
    
    def Mutation(self,parent):#parent là một individual
        child=parent
        check=True
        while check:
            randGen=r.choice(self.set_of_city)
            if (randGen not in child.chromosome):
                a=r.randint(0,self.pop_dimension)
                child.chromosome[a]=randGen
                check=False
                break
        return child
        
        
    def Offspring(self):
        offspring=[]
        while len(offspring)<self.nInd:
            parent1=r.choice(self.population.pop)
            parent2=r.choice(self.population.pop)
            rand=r.random()
            if parent1.skill_factor==parent2.skill_factor or rand<self.pMutation:
                offspring.extend(self.Crossover(parent1,parent2))
                self.crossover+=1
            else:
                offspring.append(self.Mutation(parent1))
                offspring.append(self.Mutation(parent2))
                self.mutation+=1
        return offspring
    def Selection(self):
        new_generation=[]
        fitnessTable=[[]for i in range(len(self.listTask))]
        for i in range(len(self.listTask)):
            fitnessTable[i]=sorted(self.population.pop,key= lambda x:x.factorial_cost[i])
        new_generation.extend(fitnessTable[0][:50])
        while len(new_generation)<=self.nInd:
            for j in fitnessTable[1]:
                if j not in new_generation:
                    new_generation.append(j)
        return new_generation
#--------------------------------------------------
    def run(self):
        self.population.init_pop(self.set_of_city)
        print(self.population.pop)
        self.population.update_rank()
        print("bắt đầu lặp")
        while self.iteration < 1000:
            print('thế hệ thứ',self.iteration)
            Offspring=self.Offspring()
            print('đã sinh con')
            self.population.pop.extend(Offspring)
            print('đã xác nhập')
            self.population.pop= self.Selection()
            print('đã chọn thế hệ tiếp')
            self.population.update_rank()
            print('đã đánh giá thế hệ')
            self.iteration+=1
        best=self.population.getBestIndiOfTask(self.listTask[0])
        for i in best.chromosome:
            print(i.number)
        # đến đây chỉ cần chích xuất ra kết quả
            
#-----------------------------------------------           
task1=task.Task(6)
task2=task.Task(10)
listTask=[task1,task2]
# đặt các đỉnh
set_of_city=[]
f=open("C:\\Users\\Laptop NamPhong\\Desktop\\MFO_TSP\\data\\tsp\\berlin52.tsp")
for i in range(6):
    a=f.readline()
for i in range(10):
    b=f.readline()
    b=list(b.split("\n"))
    c=[int(float(i)) for i in list(b[0].split(" "))]
    city=gen.Gen(c[0],c[1],c[2])
    set_of_city.append(city)
mfea=MultiTasking(listTask,100,0.3,set_of_city)
mfea.run()
    
        
    