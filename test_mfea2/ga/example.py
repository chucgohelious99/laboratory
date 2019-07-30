# -*- coding: utf-8 -*-
class Man:
    def __init__(self,name,age,telephone):
        self.name=name
        self.age=age
        self.telephone=telephone
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPhone(self):
        return self.telephone

chuc=Man('chuc',21,'0326129240')
print(chuc.name)
