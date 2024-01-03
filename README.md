# Analyse du Protocole de Génération de Secret par Puzzles Cryptographiques

## Auteurs
- Yvan Allioux
- Abir Hsaine

## Lancement des Scripts

### Choix du Programme dans le Dockerfile

### CMD ["/bin/bash"]

Lance un shell Bash à l'exécution du conteneur

### CMD ["python", "main.py", "1000"]

Lance main.py avec un n de 1000

### CMD ["python", "modification.py", "1000"]

Lance modification.py avec un n de 1000

### CMD ["./auto.sh"]

Lance un script pour obtenir un fichier csv des temps de calculs du programme main.py (à modifier pour modification.py) avec plusieurs lancements. Les n changent à chaque lancement avec un incrément de 100 sur un intervalle de 100 à 3000 (utile pour retrouver les graphiques)


## Build du Dockerfile

docker build -t secret_generation_with_cryptographic_puzzles -f Dockerfile.python .

## Lancement du Build

docker run -it secret_generation_with_cryptographic_puzzles

## Introduction
Ce projet explore un protocole basé sur des puzzles cryptographiques pour des communications sécurisées. Le protocole permet à deux parties, Alice et Bob, d'établir un secret partagé via un canal public, même en présence d'écouteurs passifs. Sa principale utilité réside dans la capacité d'échanger des clés de manière sécurisée sans secrets partagés préalablement.

## Description du Protocole

### Vue d'Ensemble
Le protocole implique qu'Alice génère des puzzles cryptographiques, que Bob résout pour trouver une clé secrète. Ce processus garantit un échange de clés sécurisé sur un canal public potentiellement compromis.

### Étapes Clés
1. **Génération des Puzzles** : Alice crée des puzzles, chacun cachant une clé secrète et un indice.
2. **Transmission des Puzzles** : Alice envoie ces puzzles à Bob via un canal public.
3. **Résolution du Puzzle par Bob** : Bob sélectionne et résout un puzzle pour trouver la clé secrète et l'indice, puis communique l'indice à Alice.
4. **Établissement d'un Secret Partagé** : Alice, utilisant l'indice, identifie la clé secrète correspondante.

### Rôles
- **Alice (Générateur de Puzzles)** : Crée des puzzles cryptographiques sécurisés.
- **Bob (Solveur de Puzzles)** : Sélectionne et résout l'un des puzzles d'Alice.

## Implémentation

### Classe `UserPuzzle`
Cette classe encapsule les fonctionnalités nécessaires pour que les utilisateurs génèrent ou résolvent des puzzles cryptographiques.

**Fonctionnalités Principales :**
- Génération de Puzzles : Génère `n` puzzles avec des clés secrètes uniques.
- Chiffrement des Puzzles : Utilise le hachage cryptographique et le chiffrement symétrique (comme l'AES).
- Résolution de Puzzles : Permet de sélectionner et de résoudre un puzzle au hasard.
- Gestion des Clés Secrètes : Maintient une correspondance entre les indices de puzzles et les clés secrètes.

## Analyse de la Charge de Travail

### Alice
- Complexité Computationnelle : Dominée par les opérations de hachage, évoluant linéairement avec le nombre de puzzles (`O(1000n)`).
- Complexité Spatiale : Croît linéairement avec le nombre de puzzles (`O(n)`).

### Bob
- Dispose d'une charge de travail significativement plus légère car il ne résout qu'un seul puzzle.

### Écouteur Passif
- Fait face à un défi computationnel (`O(1000n)`) pour briser le protocole, le rendant sécurisé contre l'écoute passive pour un grand nombre de puzzles.

## Analyse du Protocole Modifié

### Modifications
- Alice génère et mélange séparément deux listes : une pour les `pre_puzzle_key(i)` et une autre pour les `puzzle(i)`, augmentant la sécurité mais aussi la charge de travail pour Bob et un écouteur.

### Implications de Sécurité
- Le protocole modifié augmente considérablement la charge de travail pour un écouteur, renforçant la sécurité contre les attaques passives.

## Simulation et Résultats

### Méthodologie
- Simulation des opérations d'Alice, de Bob et d'un éventuel espion pour les protocoles original et modifié.
- Focus sur différentes valeurs de `n` (100, 1000, 10 000) et mesure des temps de calcul.

### Résultats
- Le temps de calcul d'Alice évolue linéairement avec `n`.
- Le temps de calcul de Bob est constant dans la version originale mais augmente dans la version modifiée.
- Un espion fait face à un temps de calcul exponentiellement plus élevé dans le protocole modifié.

### Paramètres de Sécurité
- Pour la version originale, un `n` de 1000 semble offrir un bon équilibre.
- Pour la version modifiée, un `n` légèrement plus élevé (par exemple, 2000) pourrait être plus approprié.


