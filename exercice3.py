T = int(input("enter un temps en seconde : "))


hours = T//3600
minutes = (T-hours*3600)//60
secondes = (T-hours*3600-minutes*60)


print(f"{T} = {hours} heures  {minutes} minutes  {secondes} secondes")



