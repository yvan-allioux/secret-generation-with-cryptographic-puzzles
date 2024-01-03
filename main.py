import random
import hashlib
import os
import sys
import timeit
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class UserPuzzle:
    def __init__(self, n):
        
        print("Initialise l'utilisateur avec un nombre de puzzles à générer.")
        
        self.n = n
        self.puzzles = []
        self.secret_keys = {}
        self.generate_puzzles()

    def hash_key(self, key):
        """
        Hash une clé 1000 fois en utilisant SHA-256.
        """
        for _ in range(1000):
            key = hashlib.sha256(key).digest()
        return key

    def generate_puzzles(self):
        
        print("Génère n puzzles cryptographiques.")
        print("Hash une clé 1000 fois en utilisant SHA-256.")
        
        for i in range(1, self.n + 1):
            pre_puzzle_key = os.urandom(16)  # Génère une chaîne aléatoire de 128 bits
            secret_key = os.urandom(16)      # Génère une clé secrète aléatoire de 128 bits
            puzzle_key = self.hash_key(pre_puzzle_key)
            message = f"{i}:{secret_key.hex()}".encode()
            cipher = AES.new(puzzle_key, AES.MODE_CBC)
            iv = cipher.iv
            encrypted_message = cipher.encrypt(pad(message, AES.block_size))
            self.puzzles.append((pre_puzzle_key, iv + encrypted_message))
            self.secret_keys[i] = secret_key
        random.shuffle(self.puzzles)  # Mélange aléatoirement la liste des puzzles


    def choose_puzzle(self):
        
        print("Choisi un puzzle au hasard.")
        
        return random.choice(self.puzzles)

    def solve_puzzle(self, pre_key, puzzle):
        
        print("Résout le puzzle pour obtenir l'indice et la clé secrète.")
        
        puzzle_key = self.hash_key(pre_key)
        iv, encrypted_message = puzzle[:16], puzzle[16:]
        cipher = AES.new(puzzle_key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size).decode()
        index, secret_key_hex = decrypted_message.split(':')
        return int(index), bytes.fromhex(secret_key_hex)

    def get_secret_key(self, index):
        
        print("Renvoie la clé secrète correspondant à l'indice donné.")
        
        return self.secret_keys.get(index)

def main():
    # Nombre de puzzles à générer
    n = int(sys.argv[1])

    # Mesure du temps pour la génération des puzzles par Alice
    start_time = timeit.default_timer()

    # Alice crée ses puzzles
    alice = UserPuzzle(n)

    # Mesure du temps pour la génération des puzzles par Alice
    generation_time = timeit.default_timer() - start_time

    # Mesure du temps pour la résolution des puzzles par Bob
    start_time = timeit.default_timer()

    # Bob choisit et résout un puzzle au hasard
    pre_key, puzzle = alice.choose_puzzle()
    index, secret_key = alice.solve_puzzle(pre_key, puzzle)

    # Mesure du temps pour la résolution des puzzles par Bob
    resolution_time = timeit.default_timer() - start_time

    # Vérification si Alice et Bob partagent le même secret
    assert alice.get_secret_key(index) == secret_key
    print(f"Puzzle résolu! Index: {index}, Clé Secrète: {secret_key.hex()}")

    print(f"Temps de génération des puzzles: {generation_time} secondes")
    print(f"Temps de résolution des puzzles: {resolution_time} secondes")
    #commande système pour ecrire dans un fichier
    os.system(f"echo {generation_time}, {resolution_time}, {n} >> resultats.csv")


if __name__ == "__main__":
    main()
