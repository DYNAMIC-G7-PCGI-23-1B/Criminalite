import numpy as np
import matplotlib.pyplot as plt
import random

seuil_crime_sans_controle = 0.4
seuil_crime_avec_controle = 0.7


#attribuer à chaque individu une probabilité de commettre un vol
def probabilite_pour_un_individu() :
  NdC = 10
  NdL = 10
  grille = np.random.random((NdC,NdL))
  np.set_printoptions(precision=1)
  grille_crime = np.array(grille)

  print("Une probabilité affectée à un individu: ")
  print(grille_crime)


#Si la probabilité de l'individu est supérieur ou égal au seuil de crimininalité
#Sans contrôle 
#1ère présentation : Tableau booléen (True:criminel ; False:No criminel)
#2ème présentation : Tableau binaire (1: Criminel ; 0: No criminel)
#3ème présentation : Tableau matplotlib

  bool_crime = [grille_crime >= seuil_crime_sans_controle]
  grille_bool_crime = np.array(bool_crime)
  print("Le Tableau Booléen identifiant les individus ayant fait un crime en abscence de contrôle:")
  print(grille_bool_crime)
  print("True : Criminels; False : Non Criminels")

  grille_2 = np.array(bool_crime) + 0
  print("Tableau binaire identifiant les individus ayant fait un crime en abscence de contrôle:")
  print(grille_2)
  print("1 : Criminels ; 0 : Non criminels")

   
  plt.imshow(grille,cmap='Set1')   
  plt.colorbar()

#Si la probabilité de l'individu est supérieur ou égal au seuil de criminalité
#Avec contrôle
#1ère présentation : Tableau booléen (True:criminel ; False:No criminel)
#2ème présentation : Tableau binaire (1: Criminel ; 0: No criminel)

  bool_crime_2= [grille_crime >= seuil_crime_avec_controle]
  grille_bool_crime_2 = np.array(bool_crime_2)
  print("Le Tableau Booléen identifiant les individus ayant fait un crime en présence de contrôle:")
  print(grille_bool_crime_2)
  print("True : Criminels; False : Non Criminels")

  grille_crime_3 = np.array(bool_crime_2) + 0
  print("Tableau binaire identifiant les individus ayant fait un crime en présence de contrôle:")
  print(grille_crime_3)
  print("1 : Criminels ; 0 : Non criminels")

#réalisation compteur
  compteur_1 = grille_bool_crime.sum()
  print("Le nombre de criminels en abscence de contrôle: ",compteur_1)
  compteur_2 = grille_bool_crime_2.sum()
  print("Le nombre de criminels en présence de contrôle: ",compteur_2)


#Détermination du taux de criminalité
  taux_de_criminalite_1 = (compteur_1/(NdL*NdC))*100
  print("Le taux de criminalité en abscence de contrôle est: ",taux_de_criminalite_1,"%")
  taux_de_criminalite_2 = (compteur_2/(NdL*NdC))*100
  print("Le taux de criminalité en présence de contrôle est: ",taux_de_criminalite_2,"%")
