# question 1

tab = list(map(int,input("Enter 10 nombers separé par espaces: ").split()[:10]))

estTrie = True

for i in range(len(tab)-1):
    if tab[i]>tab[i+1]:
        estTrie= False
        break


if estTrie :
    print("Oui , le tableau est trie dans l'ordre croissant")
else :
    print("Non , le tableau n'est pas trie dans l'ordre croissant")



print(tab)


# question 2 


vecteur_1 = list(map(int,input("Initialiser la premiere vecteur avec 3 nombre: ").split()[:3]))
vecteur_2 = list(map(int,input("Initialiser la premiere vecteur avec 3 nombre: ").split()[:3]))

sol= []

for i in range(3):
    p = vecteur_1[i]*vecteur_2[i]
    sol.append(p)

som = sum(sol)

print(f"le produit scalaire de deux vecteur {vecteur_1} et {vecteur_2} est : {som}")
