import random
import hashlib
import os
import sys
import timeit
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class UtilisateurPuzzle:
    def __init__(self, n):
        self.n = n
        self.pre_cles_puzzle = []  # Liste des clés de pré-puzzle
        self.puzzles = []  # Liste des énigmes
        self.cles_secretes = {}  # Dictionnaire pour stocker les clés secrètes
        self.generer_puzzles()

    def hash_key(self, cle):
        for _ in range(1000):
            cle = hashlib.sha256(cle).digest()
        return cle

    def generer_puzzles(self):
        print("Initialisation de l'utilisateur avec un nombre de puzzles à générer.")
        for i in range(1, self.n + 1):
            pre_cle_puzzle = os.urandom(16)  # Chaîne aléatoire de 128 bits
            cle_secrete = os.urandom(16)  # Clé secrète aléatoire de 128 bits
            cle_puzzle = self.hash_key(pre_cle_puzzle)
            message = f"{i}:{cle_secrete.hex()}".encode()
            cipher = AES.new(cle_puzzle, AES.MODE_CBC)
            iv = cipher.iv
            message_chiffre = cipher.encrypt(pad(message, AES.block_size))
            self.pre_cles_puzzle.append(pre_cle_puzzle)
            self.puzzles.append(iv + message_chiffre)
            self.cles_secretes[i] = cle_secrete

        random.shuffle(self.pre_cles_puzzle)
        random.shuffle(self.puzzles)

    def choisir_et_resoudre_puzzle(self):
        print("Choix d'un puzzle au hasard.")
        puzzle_choisi = random.choice(self.puzzles)
        for pre_cle in self.pre_cles_puzzle:
            cle_puzzle = self.hash_key(pre_cle)
            for i in range(self.n):
                try:
                    iv, message_chiffre = puzzle_choisi[:16], puzzle_choisi[16:]
                    cipher = AES.new(cle_puzzle, AES.MODE_CBC, iv)
                    message_dechiffre = unpad(cipher.decrypt(message_chiffre), AES.block_size).decode()
                    index, cle_secrete_hex = message_dechiffre.split(':')
                    if self.cles_secretes[int(index)] == bytes.fromhex(cle_secrete_hex):
                        print(f"Puzzle résolu! Indice : {index}, Clé Secrète : {cle_secrete_hex}")
                        return int(index), bytes.fromhex(cle_secrete_hex)
                except ValueError:
                    continue  # Continuer à essayer avec d'autres clés si le déchiffrement échoue
        raise ValueError("Impossible de résoudre aucun puzzle")

    def obtenir_cle_secrete(self, index):
        """
        Retourne la clé secrète correspondant à l'indice donné.
        """
        return self.cles_secretes.get(index)

def main():

    # premier paramètre quand on lance le script
    n = int(sys.argv[1])

    # Mesure du temps pour la génération des puzzles par Alice
    start_time = timeit.default_timer()

    # Alice crée ses énigmes
    alice = UtilisateurPuzzle(n)

    # Mesure du temps pour la génération des puzzles par Alice
    generation_time = timeit.default_timer() - start_time
 
    # Mesure du temps pour la résolution des puzzles par Bob
    start_time = timeit.default_timer()

    # Bob choisit et résout une énigme au hasard
    index, cle_secrete = alice.choisir_et_resoudre_puzzle()

    # Mesure du temps pour la résolution des puzzles par Bob
    resolution_time = timeit.default_timer() - start_time

    # Vérifier si Alice et Bob partagent la même clé secrète
    assert alice.obtenir_cle_secrete(index) == cle_secrete

    print(f"Temps de génération des puzzles: {generation_time} secondes n = {n}")
    print(f"Temps de résolution des puzzles: {resolution_time} secondes n = {n}")
    #commande système pour ecrire dans un fichier
    os.system(f"echo {generation_time}, {resolution_time}, {n} >> resultats.csv")


if __name__ == "__main__":
    main()
