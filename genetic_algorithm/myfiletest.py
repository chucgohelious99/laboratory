# -*- coding: utf-8 -*-
import GA
import numpy
pop=numpy.array([[  3.10367998,  -3.90375935,   0.13994302,  -1.8204054,  -42.69911788,
   -3.35662608],
 [  3.10367998,  -3.90375935,   0.13994302,  -1.8204054,  -42.53478262,
   -3.35662608],
 [  3.10367998,  -3.90375935,   0.13994302,  -1.8204054,  -42.40755185,
   -3.35662608],
 [  3.10367998,  -3.90375935,   0.13994302,  -1.8204054,  -42.08062816,
   -3.35662608]])
fitness=[493.86922508, 489.05685954, 485.82656547, 485.15952133, 497.07645144,
 495.26876352, 478.05569704, 490.27306445]
num_parent=8
parents=GA.select_mating_pool(pop,fitness,num_parent)
print(parents)