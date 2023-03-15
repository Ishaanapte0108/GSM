"""SRES generation by A3 algorithm"""
"""Generating RANDOM(128 bits) & Key(128 bits)"""
import random
class GSM:
    
    def random(l,num):  
        l = list(map(lambda x: random.randint(0, 1), range(num)))
        
    
    # def divide(self, executeBlock):
        
    #     if executeBlock == 1:
    #       mid = self.n // 2
    #       self.r1[:mid] = self.randomBits[:mid]  
    #       self.r2[:mid] = self.randomBits[mid:]  
    #       self.k1[:mid] = self.key[:mid]
    #       self.k2[:mid] = self.key[:mid]

    #     if executeBlock==2:
    #       mid = self.n // 2 // 2
    #       self.subOperation1[:mid] = self.r1[:mid]  
    #       self.subOperation2[:mid] = self.r1[mid:]  
      
    # def XOR(self,executeBlock):
        
    #     if executeBlock == 1:
    #       self.r1 = list(map(lambda a, b: a ^ b, self.r1, self.k2))
    #       self.r2 = list(map(lambda a, b: a ^ b, self.r2, self.k1))
    #       self.r1 = list(map(lambda a, b: a ^ b, self.r1, self.r2))
        
    #     if executeBlock == 2:
          
    #       self.subOperation1 =  list(map(lambda a, b: a ^ b, self.subOperation1, self.subOperation2))

n = 128
randomBits = []
key = []
r1 = []
r2 = []
k1 = []
k2 = []
subOperation1 = []
subOperation2 = []
randomBitsForSim = []

g = GSM()
g.random(randomBits,n)

print(randomBits)