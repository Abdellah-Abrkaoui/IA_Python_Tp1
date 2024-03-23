age = int(input("Entrer votre age :"))
sexe = (input("Entrer votre sexe \"m\" ou \"homme\",  \"f\" ou \"femme\" :").strip().lower())[0]

while age >0 and sexe == "f" or sexe =="m":
    if age >=20 and sexe =="m" :
        print("vous etes homme de plus de 20 ans ! tu doit payez l'impot")
        break
    elif age>=18 and age<=35 and sexe =="f" :
        print("vous etes femme entre 18 ans et 35 ans ! tu doit payez l'impot")
        break
    else :
        print("tu doit pas payez l'impot")
        break






