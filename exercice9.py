n = int(input("enter un nombre entier non null : "))
sol = []

if n > 0:
    for item in range(1,n):
        if(n%item == 0):
            sol.append(item)



som = 0
for i in sol :
    som = som+i


if som == n:
    print(f"{n} est un nombre parfait ")
else :
    print(f"{n} n'est pas un nombre parfait")

