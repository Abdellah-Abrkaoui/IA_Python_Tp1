import math

def equation(a,b,c):
    delta =  (b*b) - 4*a*c

    if delta <0:
        print("no solution")
    elif delta == 0 :
        sol = (-b/2*a)
        print(sol)
    else :
        sol1 = (-b+ math.sqrt(delta))/2*a
        sol2 = (-b- math.sqrt(delta))/2*a
        print("sol 1 = {:.2f} et sol 2 = {:.2f} ".format(sol1,sol2))
equation(2,7,2)





