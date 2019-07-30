 # -*- coding: utf-8 -*-
import node
import MultiTaskingGA as mul
import sys
sys.path.append('C:\\Users\\Laptop NamPhong\\python file\\laboratory\\situation2_wrsn_mfea\\task')
import Situation2 as sit
import TSP as tsp

set_of_city=[]
f=open("data.txt")
for i in range(21):
    b=f.readline()
    b=list(b.split("\n"))
    c=[float(i) for i in list(b[0].split(" "))]
    city=node.Node(c[0],c[1],c[2],c[3],c[4])
    set_of_city.append(city)
    
task1=sit.Situation2(21)
task2=tsp.TSP(20,set_of_city)
tasks=[]
tasks.append(task1)
tasks.append(task2)

mfea=mul.MultiTasking(tasks,100,0.5,50)
mfea.run(100,set_of_city)