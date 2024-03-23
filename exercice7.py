import math
n = int(input("enter un nombre entier non null : "))
sol=[]
if n >= 0 :
    for item in range (1,n+1) :
        somme = int(math.pow(item,2))
        sol.append(somme)


som = 0
for i in sol :
    som = som+i



print(f"la somme des {n} premier carrés est : {som}")







