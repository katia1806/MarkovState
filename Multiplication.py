import numpy as np

#fonction du produit matriciel de tableaux de tableaux sans l'utilisation de numpy
def multiply(m1, m2):
  m = []
  if len(m1[0]) != len(m2):
    print ("Erreur! Le produit matriciel est impossible.") #Le produit matriciel est impossible dans ce cas
    return False
  for i in range(len(m1)):
    ligne = []
    for j in range(len(m2[0])):
      element = 0
      for k in range(len(m1[0])):
        element = element + m1[i][k] * m2[k][j]
      ligne.append(element)
    m.append(ligne)
  return m

#recupération des données entrées par l'utilisateur
print("Bonjour, on vas calculer Xn= X0 x P^n.")

print("Choisissez le nombre d'états:")
Nmbr=input()

print("Quel état souhaitez vous claculer \n n=")
n=input()

test= True
while bool(test) : #Boucler tant que l'état initial ne figure pas dans les états existants
    print("Quel est l'état initial \n X0=")
    X0=input()

    if 0 < int(X0) <= int(Nmbr):

        test = False
        #Transformation de l'état initial en un vecteur
        Vect=[0 for i in range(int(Nmbr))]
        for i in range(0,int(Nmbr)):
            if i +1 == int(X0):
                Vect[i]= 1
            else :
                Vect[i]= 0

        #Lecture de la matrice carrée P entrée par l'utilisateur
        print("Entrez la matrice de transition carrée P: ")
        M= [[0 for i in range(int(Nmbr))] for j in range(int(Nmbr))]
        for i in range( 0, int(Nmbr)):
            for j in range(0,int(Nmbr)):
                print("La valeur P[i=",i,",j=",j,"]=")
                M[i][j]=int(input())

        #Appel de la fonction de multiplication n fois
        power=M # Initialisation de la matrice P^n
        for i in range(1 , int(n)):
            power= multiply(power,M) #Calcul de la matrice P^n

        #Utilisation de la methode asarray() de NumPy pour convertir les tableaux en array
        #Utilisation de la methode dot() pour réaliser le produit du vecteur X0 par la matrice P^n
        powerV=np.dot(np.asarray(Vect),np.asarray(power))

        print("X",int(n),"=",powerV)

    else:
        print("Erreur! Choisissez un état initial existant.")