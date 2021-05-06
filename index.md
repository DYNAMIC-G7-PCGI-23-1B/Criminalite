

# La criminalité

Notre objectif est de modéliser une population commettant des crimes afin de prévenir celle-ci. Le terme "crime" est très vaste. En effet, cette notion n'est pas perçue de la même manière d'une culture à une autre. Il existe différents types de crime : crime contre l'humanité, crime contre la justice, crime contre l'État etc. Par choix arbitraire, nous avons choisi de nous concentrer sur le crime contre le bien personnel comme par exemple le vol qualifié. Cependant, est-il possible de réguler le taux de vol dans une population ? Dans un premier temps, nous avons réalisé un modèle où des individus d'un quartier commettent des vols sans aucun dispositif de sécurité (policier, caméra, agent de sécurité...). Chaque individu est affecté à une probabilité de commettre un crime. Afin d'augmenter la difficulté de notre modèle, nous avons ensuite considéré l'influence des voisins commettant un crime sur un autre individu au tour suivant.
Dans un second temps, nous allons réaliser les mêmes types de modèles mais en présence de dispositifs de sécurité.
Dans ces parties nous verrons que le taux de vols diminuera effectivement lors de l'installation de dispositiifs de sécurité.


Résumé de quelques lignes présentant l'objectif de votre projet, la méthode que vous avez suivie pour le réaliser et les résultats marquants que vous avez obtenus.

## English version

Our goal is to model a population committing crimes in order to prevent it. The term "crime" is very broad. Indeed, this notion is not perceived in the same way from one culture to another. There are different types of crime: crime against humanity, crime against justice, crime against the state, etc. By arbitrary choice, we have chosen to focus on crime against personal property such as robbery. However, may the rate of theft in a population be regulated? At first, we created a model where individuals from a neighbourhood commit robberies without any security devices (policemen, cameras, security guards...).Each individual is assigned to the probability of committing a crime. In order to increase the difficulty of our model, then, we considered the case where the acts of one person may influence or not another person to commit a crime too.
 In a second part, we will make the same types of models but in the presence of safety devices as police,camera, security guard etc.  
## Présentation de l'équipe

|(´・ω・｀)| ( ͡° ͜ʖ ͡°) | ಠ_ಠ | ᕕ( ᐛ )ᕗ |
|-----|--|--|--|
| D. Preville| C. Rouaa | J. Marques  | F. Demotes-Mainard  |


## Description synthétique du projet

**Problématique : Comment peut-on réguler le taux de vol dans une population ?** 

**Hypothèse principale : Les dispositifs de sécurités peuvent être un régulateur du taux de vol.**
 

**Objectifs : Prévenir la criminalité**


## Présentation structurée des résultats

### Taux de vols en absence de sécurité

Nous avons décidé de nous inspiré du modèle de Schelling. Nous avons pour cela créer une grille 2D numpy où chaque individu possède une probabilité générée au hazard par  ```` np.random.random ```` . Celle-ci correspond à la chance d'un individu de commettre un vol.
 Nos paramètres généraux : 
 ```` 
      seuil_crime_sans_controle : seuil à ne pas dépasser sinon individu considéré comme criminel potentiel
      NdL : Nombre de lignes dans la grille
      NdC : Nombre de colonnes dans la grille 
      NdC* NdL correspond à la taille de la grille soit le nombre d'habitants dans ce quartier
 ````
 Nous avons repéré des sous paramètres concernant le ````seuil_crime_sans_controle```` :
 
      - le niveau de vie du quartier

      - crise (économique, sanitaire, politique...)
 
Considérons plusieurs types de quartier composé de 100 habitants :
|.    | Quartier aisé | Quartier modeste | Quartier défavorisé |
|-----|--|--|--|
| ````seuil_crime_sans_controle````| ````0,7```` | ````0,5````  | ````0,4````  |

Les grilles que l'on observe avec ````0 : Non criminels ; 1 : Criminels ```` :
   - Quartier aisé :

````[[[0 0 0 1 1 1 0 0 0 0]
  [0 0 0 0 0 1 1 1 0 0]
  [1 1 0 0 1 0 0 1 0 0]
  [0 1 0 1 0 1 0 0 0 1]
  [0 1 0 1 0 0 0 0 0 0]
  [0 0 1 0 1 1 1 0 0 0]
  [0 0 0 0 0 0 0 0 1 1]
  [0 1 0 0 1 0 0 1 0 0]
  [0 0 0 0 0 1 0 1 0 1]
  [0 1 0 0 0 0 1 1 0 0]]]
  
  Le nombre de criminels en absence de contrôle:  31
  ````


   - Quartier modeste :
 ````[[[0 0 0 1 0 1 0 1 1 0]
  [1 1 1 1 0 0 1 1 1 0]
  [0 1 1 0 0 0 1 0 0 0]
  [1 0 1 0 0 0 1 0 0 0]
  [0 1 0 0 0 1 1 0 0 0]
  [0 0 0 0 0 0 0 1 0 0]
  [0 1 1 1 1 1 0 1 0 0]
  [1 0 1 0 1 0 0 0 1 1]
  [1 1 0 1 1 1 0 0 0 0]
  [1 0 1 1 0 0 0 1 1 0]]]
  
  Le nombre de criminels en absence de contrôle:  42
  ````


  - Quartier défavorisé : 
   
 
````[[[0 0 0 0 0 0 0 1 0 1]
  [1 0 1 1 0 1 1 0 0 1]
  [0 1 0 0 1 0 1 0 1 1]
  [1 0 1 1 0 1 1 0 1 1]
  [1 0 0 1 1 1 1 1 0 0]
  [0 1 1 1 0 1 1 1 0 1]
  [1 1 1 1 0 0 1 1 1 1]
  [1 1 1 0 0 1 0 1 1 1]
  [0 1 1 0 1 1 1 1 0 0]
  [0 1 0 1 1 0 1 0 1 1]]]
  
  Le nombre de criminels en absence de contrôle:  60
````
Remarque : Le nombre de criminels a été généré grâce à ce compteur :
````
compteur_1 = grille_bool_crime.sum()
```` 
### Calcul taux de vol pour 100 habitants :
   - Formule :
````
taux_de_criminalite_1 = (compteur_1/(NdL*NdC))*100
```` 
   - Résultats :
 
|.    | Quartier aisé | Quartier modeste | Quartier défavorisé |
|-----|--|--|--|
| ````taux_de_criminalité_1 (en %)````| ````31```` | ````42````  | ````60````  |


### Observation :
Pour une population de 100 habitants, on observe qu'il est plus probable de commettre un vol dans un quartier défavorisé que dans un quartier aisé.Il peut y avoir plusieurs raisons : population plus jeune dans les quartiers défavorisés, faible pouvoir d'achat,taux de chômage plus important... Cependant, même s'il existe un grand écart entre ces types de quartier, est ce que cela signifie que les vols commis dans les quartiers aisés sont moins dangereux que ceux commis dans les quartiers défavorisé ? Ou bien est-ce que les revenues d'une personne sont-elles vraiment un facteur afin de justifier un crime commis ? Nous faisons le choix de ne pas l'aborder. 

Considérons maintenant une population des différents quartiers en situation de crise sanitaire par exemple :

|.    | Quartier aisé | Quartier modeste | Quartier défavorisé |
|-----|--|--|--|
| ````seuil_crime_sans_controle````| ````0,6```` | ````0,4````  | ````0,3````  |

Les grilles que l'on observe avec ````0 : Non criminels ; 1 : Criminels ```` :
   - Quartier aisé :

````[[[1 0 0 0 0 1 0 0 0 0]
  [0 0 1 1 1 0 1 1 0 0]
  [0 0 1 0 0 0 1 0 1 0]
  [0 0 0 1 0 0 1 1 0 1]
  [0 1 0 0 0 1 0 0 0 0]
  [0 1 1 0 1 1 0 0 1 1]
  [1 0 1 1 0 0 1 0 1 0]
  [0 1 1 1 1 1 0 1 0 0]
  [0 0 1 1 0 0 0 0 1 1]
  [0 0 1 0 1 1 0 0 0 1]]]
  
  Le nombre de criminels en absence de contrôle:  41
  ````


   - Quartier modeste :
 ````  [[[[1 1 0 1 0 1 1 1 0 1]
  [0 1 1 0 0 0 0 1 0 1]
  [0 1 1 0 1 1 1 0 0 0]
  [1 1 0 0 0 0 1 1 0 1]
  [0 0 1 0 1 0 1 0 1 0]
  [1 0 0 1 1 1 1 0 0 0]
  [0 1 1 0 1 1 0 1 0 1]
  [1 0 0 1 0 1 1 1 1 1]
  [0 1 1 0 1 0 1 0 1 1]
  [1 0 1 1 1 1 1 0 1 1]]]
  
  Le nombre de criminels en absence de contrôle:  57
  ````


  - Quartier défavorisé : 
   
 
````[[[1 1 0 0 0 1 1 0 0 1]
  [1 1 1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1 0 1]
  [0 1 1 1 1 1 1 1 0 1]
  [0 1 1 1 1 1 0 0 0 1]
  [0 1 1 0 1 1 1 1 1 1]
  [1 1 1 0 0 1 1 0 0 0]
  [0 1 1 1 0 1 1 0 1 0]
  [1 0 0 1 1 1 0 1 1 1]
  [1 1 1 1 1 0 1 0 1 1]]]
  
  Le nombre de criminels en absence de contrôle:  72
````
### Calcul taux de vol en situation de crise
- Résultats :
 
|.    | Quartier aisé | Quartier modeste | Quartier défavorisé |
|-----|--|--|--|
| ````taux_de_criminalité_1 (en %)````| ````41```` | ````57````  | ````72````  |

### Observation

On constate la même chose. En effet, le seul de criminalité est toujours élevé dans les quartiers aisés.



Présentation du choix de modélisation, des outils, du code et des résultats (tableaux, courbes, animations...) (**avec une analyse critique**).

## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :
https://fr.wikipedia.org/wiki/Crime#Grandes_catégories_de_crimes

https://www.insee.fr/fr/metadonnees/definition/c2048

https://www.cairn.info/revue-reseaux-2017-6-page-95.htm

https://www.scienceshumaines.com/pourquoi-la-criminalite-chute_fr_31470.html

https://www.cairn.info/revue-reseaux-2018-5-page-221.htm

## Carte mentale de nos mots-clés :

![Unknown](https://user-images.githubusercontent.com/80456390/116925134-163b8b80-ac59-11eb-9e3f-1ef410f67a19.png)

