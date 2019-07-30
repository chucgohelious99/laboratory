# -*- coding: utf-8 -*-
#  đọc vào dữ liệu các node
# đọc vào dữ liêu con đường tốt nhất bestWayIndex[]
# lưu trữ lại bestWayIndex[] dưới dạng mảng bestWay[]
import population
import node
E_max=8000
E_min=540
E_mc=80000
U=5
setGen=[]
bestWayIndex=[]
try:
    f=open("u100-result.txt")
    for i in range(1,101):
        a=f.readline()
        a=a.split('\n')
        c=a[0].split(' ')
        b=[]
        for i in range(len(c)):
            b.append(float(c[i]))
        setGen.append(node.Node(i,b[0],b[1],b[2],b[3],E_max,E_min,U))
    a1=f.readline()
    a1=a1.split('\n')
    c1=[int(x) for x in a1[0].split(' ')]
    bestWayIndex=c1
finally:
    f.close()
bestWay=[]
for index in bestWayIndex:
    index=int(index)
    for nod in setGen:
        if nod.number==index:
            bestWay.append(nod)
lengWay=bestWay[0].distanceToPole()+bestWay[99].distanceToPole()
for i in range(99):
    lengWay+= bestWay[i].distanceTo(bestWay[i+1])
E_t=lengWay/5
to=(E_mc-E_t)/U
nPop=100
nNode=100
exe=population.Population(bestWay,nPop,nNode)
exe.run(bestWay,to,E_max,E_min,lengWay)