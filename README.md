
# secret-generation-with-cryptographic-puzzles

# Accréditation Anonyme avec le 3-Coloriage de Graphe

## 1. Introduction

Ce projet porte sur l'implémentation d'une accréditation anonyme via une preuve de connaissance à divulgation nulle basée sur le problème du 3-coloriage de graphe. Le but principal est de permettre à un utilisateur de prouver qu'il connaît une solution de coloriage d'un graphe en trois couleurs, où aucun nœud adjacent n'est de la même couleur, sans pour autant révéler d'informations sur le coloriage lui-même.

## 2. Implémentation du Programme

### a. Génération du Graphe et Coloriage

- La fonction `genererGraphe3Coloriable` sert à générer un graphe qui peut être colorié avec trois couleurs.
- Le coloriage des nœuds est effectué aléatoirement en choisissant parmi les couleurs "rouge", "vert", et "bleu".
- Une matrice d'adjacence est créée, en évitant de connecter les nœuds de la même couleur.

### b. Mise en Gage des Couleurs

- La fonction `miseEnGageColoriage` prend en entrée les couleurs des nœuds et des valeurs aléatoires pour retourner un tableau de valeurs mises en gage.
- Ces valeurs sont créées en concaténant chaque couleur avec une valeur aléatoire et en hachant le résultat.

### c. Preuve de Connaissance à Divulgation Nulle

- La fonction `preuveColoriage` vérifie si un utilisateur connaît le coloriage d'un graphe en utilisant un protocole de vérification.
- Après avoir soumis une mise en gage de son coloriage, l'utilisateur doit révéler les couleurs de deux nœuds spécifiés par le vérificateur.

## 3. Analyse du Protocole

### a. Propriété de Completeness

- Si l'utilisateur et le vérificateur suivent le protocole correctement, l'utilisateur parviendra toujours à convaincre le vérificateur. Ceci est dû au fait que le graphe est 3-coloriable par conception, et l'utilisateur connaît le coloriage correct.

### b. Propriété de Soundness

- Un utilisateur sans connaissance du 3-coloriage aurait une chance négligeable de tromper le vérificateur, car il lui serait impossible de générer un engagement valide sans cette connaissance.

### c. Propriété de Zero-Knowledge

- Le protocole est à divulgation nulle car il ne révèle aucune information sur le coloriage réel, à part le fait que l'utilisateur le connaît. Le vérificateur ne voit que des valeurs mises en gage (sous forme de hachages) et deux couleurs de nœuds adjacents à chaque étape.

## 4. Conclusion

Ce TP offre une introduction concrète aux concepts d'accréditation anonyme et de preuves à divulgation nulle, essentiels pour la sécurité et la confidentialité dans les interactions numériques. L'implémentation suit fidèlement le protocole défini.

## Instructions pour Docker

Pour utiliser ce projet avec Docker, suivez ces étapes :

1. **Construction de l'Image Docker** :
   
   Exécutez la commande suivante pour construire l'image Docker :


```docker build -t secret_generation_with_cryptographic_puzzles -f Dockerfile.python .```


2. **Exécution du Conteneur Docker** :

Pour lancer le conteneur Docker, utilisez :

```docker run -it secret_generation_with_cryptographic_puzzles```


3. **Exécution du Programme** :

Dans le conteneur Docker, lancez le programme avec :

```python main.py```
