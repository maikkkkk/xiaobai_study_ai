# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:59:45 2020

@author: 37494
"""
class a:
    def __init__(self):
        self.age=100
        
    def add(self):
        self.age=self.age+1
    def show(self):
        print(self.age)
        return 0

b=a()
if b.show()==0:
    print("nihao")