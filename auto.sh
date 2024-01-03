#!/bin/bash

# Boucle for pour exécuter la commande 100 fois avec un incrément de 100 pour le paramètre
for ((parametre=100; parametre<=3000; parametre+=100)); do
    python3 main.py "$parametre" > /dev/null
    echo $parametre
done
