# -*- coding: utf-8 -*-
import population as pop
import node 
import time

v=0
p_m=0
e_m=0
U=0
nIndi=100
iteration=100
# creat set of node and pole
pole=node.Node(0,0,0,0,10800)
set_of_node=[]

start=time.time()
runGA=pop.Population(nIndi,set_of_node)
runGA.initial()
for i in range(iteration):
    print('this is generation',i)
    runGA.printBestIndi(set_of_node,pole,v,p_m,e_m)
    children=runGA.generateChildren()
    runGA.selection(children)
end=time.time()
f=open('result.txt')
f.writelines('time execution for 1 try is',start-end)
f.close
    
