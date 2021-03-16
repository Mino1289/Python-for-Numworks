# Python-for-Numworks
Programmes Python pour la calculatrice <a href="https://www.numworks.com/">Numworks</a>.  

## Comment installer mathsup ou physicsup ?
1. Installation  
UNIQUEMENT AVEC CHROME :   
Premièrement, allez sur mon workshop de numworks, <a href="https://workshop.numworks.com/python/mino-1289/">ici</a>.  
Branchez votre calculatrice, choisissez un programmes puis cliquez sur le bouton `Envoyer sur ma calculatrice`.  

2. Utilisation des commandes  
Maintenant que vous avez installé mathsup et/ou physicsup, vous pouvez les utiliser :  
Débranchez votre calculatrice de votre ordinateur, et ouvrez l'application Python.  
Puis vérifiez que seul mathsup et physicsup sont importé dans la console.  
Pour le vérifier, sur chaque script, allez sur les `...` et appuiez sur `OK` ou `EXE`.  
Vérifiez que seul mathsup et physicsup ont le boutons cochés pour l'auto-importation dans la console.  
A présent allez dans la console d'execution de Python  
Appuyez sur `var`, choisissez une fonction et appyez sur `OK` ou `EXE`
Complétez la fonction qui viens de s'afficher dans la console avec les paramètres, séparé par des virgules.
Puis appuyez sur `OK` ou `EXE`, votre fonction c'est lancé.

### Toutes les fonctions :
Passer votre souris sur le nom de la fonction pour retrouver le code dans les fichiers.  
```py
from mathsup import *
from physicsup import *
# mathsup :
>>> arran(n,k) # renvoie le nombre d'arrangement de k élement parmi n

>>> bin_int(n) # renvoie l'entier correspondant au nombre binaire n

>>> combi(n,k) # renvoie le nombre d'élément à k élément parmi n

>>> cong(a,n) # renvoie le couple (b, c), les entiers les plus proche de 0 congru à a modulo n,
              # soit a ≡ (b, c) [n] (b est positif, pas c)  

>>> congi(a,n) # renvoie b, le plus proche entier congru à a modulo n, soit a ≡ b [n] (b peut être négatif)  

>>> dioph(a,b) # renvoie un couple (u, v), tel que a*u+b*v = 1  

>>> dioph(a,b,c) # renvoie un couple (u,v) tel que a*u+b*v = c  

>>> disc(a,b,c) # renvoie b²-4*a*c  

>>> dive(a,n) # renvoie le couple de la division euclidienne de a par n

>>> divint(n) # renvoie une liste de tous les entiers qui divisent n

>>> fact(n) # renvoie n!

>>> factor(n) # renvoie la liste de tous les facteurs premiers de n

>>> int_bin(n) # renvoie n en binaire

>>> iscong(a,b,n) # renvoie Vrai/Faux si a ≡ b [n]

>>> log16(n) # renvoie le logarithme base 16 de n

>>> permut(n) # renvoie toutes les permutations d'un ensemble de taille n (soit n!)

>>> pgcd(a,b) # renvoie le plus grand diviseurs commun à a et b

>>> ppcm(a,b) # renvoie le plus petit multiple commun à a et b

>>> prime(n) # renvoie Vrai/Faux si n est un nombre premier

>>> q(a,n) # renvoie le quotient entier de la division euclidienne de a par n

>>> r(a,n) # renvoie le reste de la division euclidienne de a par n, toujours positif

>>> tp(x,y,z) # renvoie Vrai/Faux, si x,y,z est un triplet pythagoricien.


# physicsup :
>>> pvnrt(p,v,n,t) # renvoie la valeur que vous lui demandez dans sa construction : exemple :
                   # mettez "" à la valeur que vous voulez calculer pour P*V = n*R*T

>>> pvnrt(1000, "", 5, 400) -> V = 16.62 m^3  

>>> rho(m,V,p) # Même principe, mais pour p = m/V 
```
## Les autres programmes
* Informations
  * Téléchargement
  UNIQUEMENT AVEC CHROME :   
  Pour télécharger ces programmes, rendez-vous sur mon workshop chez numworks, <a href="https://workshop.numworks.com/python/mino-1289/">ici</a>.  
  Branchez votre calculatrice, choisissez le(s) programme(s) que vous souhaitez sur votre calculatrice et appuyez sur `Envoyer sur la calculatrice`.  
  C'est fini !  
  * Utilisation 
   Pour faciliter l'utilisation, il est préférable d'éxécuter chaque script séparément, soit ne pas les importer dans la console.  
  Pour ça allez dans le script que vous voulez lancer, allez dans les paramètres du script `...` avec `OK` ou `EXE`.  
  Et décochez l'option auto-importation dans la console, puis appuyez sur `Exécuter le script` avec `OK` ou `EXE`.  
  Ce sera la seule façon de lancer ces programmes. Et maintenant
 

* Maths  
  * congtest.py  
  Fais un tableau de congruence pour vous, il vous suffit de rentrer les valeurs demandés. (mathsup requis
  * crypto.py  
  Crypte un message en fonction du jour dans le mois que nous sommes. (basée sur exercices du cours) (mathsup requis)
  * discriminant.py  
  Calcul du discriminant, vous donnez a,b,c et le reste est automatique. (mathsup requis)
  * racinen.py  
  Renvoie les racines n-ième de l'unité de Z^n = 1, vous donnez n.
* Physique-Chimie  
  * xmax.py  
  Calcul xmax dans une equation avec max : 3 réactifs, quantité de matière modifiable, coeficient stoechiométrique modifiable.  
  Renvoie ce qui reste des autres reactifs.
  * atom.py  
  Donnez un atome Z = n, et donne les informations importante sur cet atome.  
  Obsolète avec Omega OS  
  

#### Des questions ?
Envoyez moi un message sur Discord : `Mino#1289`  
Ou créez une issue et expliquez votre problème :)
