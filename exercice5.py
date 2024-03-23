number1 = int(input("Enter le premier nombre : "))
number2 = int(input("Enter le deuxieme nombre : "))
operator = input("Enter l'operateur \"+\" , \"-\" , \"*\" ou \"/\"  : ")

if operator =="+":
    solution = number1+number2
    print(solution)

elif operator =="-" :
    solution = number1-number2
    print(solution)

elif operator =="/" :
    solution = number1/number2
    print(solution)

elif operator =="*" :
    solution = number1*number2
    print(solution)

else :
    print("operator invalid")

