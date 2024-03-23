notes = []
for note in range(1,4) :
        while True :
            num = input(f"enter la {note} note : ")
            num = int(num)
            if num>=0 and num<=20 : 
                notes.append(num)
                break
            
moyen = int(sum(notes))/3
print(moyen)
if moyen >= 16:
     print("Tres bien")
elif moyen >=14 :
     print("bien")
elif moyen >=12 :
     print("assez bien")
elif moyen >=10:
     print("passable")
else :
     print("insufisant")         



