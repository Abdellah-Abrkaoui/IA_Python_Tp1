import math

n= int(input("enter un nombre n entier positive : "))

sol =  []

if n>= 0:
    for item in range(0,n+1):
        somme = int(math.pow(10,item))
        # print(somme)
        sol.append(somme)
        
som = 0
for i in sol :
    som = som+i



print(f"la somme S est  : {som}")

