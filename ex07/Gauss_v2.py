
nbrInput = int(input ("Quel est votre nombre ? :\n"))
def gauss (nbrInput) :
  nbr = 1
  nbrSomme = 1
  while (nbr < nbrInput) :
    nbr += 1
    nbrSomme += nbr
  print (f"Nous allons calculer la somme de tous les nombre de 1 jusqu'à {nbrInput}\nLe résultat est {nbrSomme}")

gauss (nbrInput)