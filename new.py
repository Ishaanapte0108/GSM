import random

num =128

def randomNumbers(n):
   return list(map(lambda x: random.randint(0,1), range(n)))

def divide(list):
   mid = len(list)//2
   return (randomBits[:mid],randomBits[mid:])

def xor(list1, list2):
   return list(map(lambda x,y: x^y, list1,list2))

"""SRES generation by A3 Algorithm"""
randomBits = randomNumbers(num)
key = randomNumbers(num)
print("Random & key",randomBits, key)
r1,r2 = divide(randomBits)
k1,k2 = divide(key)
r1 = xor(r1,k2)
r2 = xor(r2,k1)
r1 = xor(r1,r2)
subop1,subop2 = divide(r1)
subop1 = xor(subop1,subop2)
"""Accept random for string"""
randomBitsSIM = randomBits
print("Enter random bits of sim: ", randomBitsSIM)
keySIM = key
print("Eneter key of sim: ", keySIM)
r1SIM, r2SIM = divide(randomBitsSIM)
k1SIM, k2SIM= divide(keySIM)
r1SIM = xor(r1SIM,k2SIM)
r2SIM = xor(r2SIM, k1SIM)
r1SIM = xor(r1SIM,r2SIM)
subopSIM1, subopSIM2 = divide(r1SIM)
subopSIM1= xor(subopSIM1,subopSIM2)
if subop1==subopSIM1:
   print('Authenticated')
else:
   print("NOT Authenticated")


