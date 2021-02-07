# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:31:18 2021

@author: Aleksy
"""
import numpy as np
import random
from matplotlib.pyplot import *
rcParams['figure.figsize'] = [15, 15]
matplotlib.rcParams.update({'font.size': 20})


class fight:
    def __init__(self, n=2):
        self.n = n
        self.initHeroes()
        self.stertGame()
        
    def initHeroes(self):
        self.heroes = dict()
        for i in range(self.n):
            self.heroes[f'player {i+1}'] = 100
        self.alive = list(self.heroes.keys())
        
    def deffence(self, p=0.5):
        rand = np.random.uniform(0,1)
        if rand < p:
            return True
        else:
            return False
            
    
    
    def stepInFight(self):
        allreadyA = []
        for i in range(self.n):
            queueAgressor = list(self.alive)
            try:
                queueAgressor.remove(allreadyA)
            except:
                pass
            queueVictom = list(self.alive)
            agressor = random.choice(list(queueAgressor))
            queueVictom.remove(agressor)
            allreadyA.append(agressor)
            try:
                victom = random.choice(list(queueVictom))
                while victom not in self.alive:
                    victom = random.choice(list(queueVictom))
                hit = np.random.uniform(0,10)
                deff = self.deffence()
                if deff:
                    self.heroes[victom] = self.heroes[victom] - hit
                    if self.heroes[victom] <= 0:
                        self.heroes[victom] = 0
                        self.alive.remove(victom)
            except:
                pass
                    
    def plotThis(self):
        for i in range(self.n):
            plot([0,self.heroes[f'player {i+1}']], [i+1,i+1])
            xlim(0, 100)
            legend([f'player {i+1}' for i in range(self.n)])
        show()
        
    def stertGame(self):
        while len(self.alive) > 1:
            self.stepInFight()
            self.plotThis()
                
      

if __name__=="__main__":
    fight()
    