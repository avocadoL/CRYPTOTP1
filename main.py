#!/usr/bin/env python3

import caesarscript
import scytale
import polybius
import affine
import vigenere

def test_caesar():
    print("\n=== TEST DU CHIFFREMENT DE CÉSAR ===")
    texte_clair = "HELLO"
    decalage = 3
    print(f"Texte original : {texte_clair}")
    print(f"Décalage : {decalage}")
    
    chiffre = caesarscript.caesar_encrypt(texte_clair, decalage)
    print(f"Texte chiffré : {chiffre}")
    
    dechiffre = caesarscript.caesar_decrypt(chiffre, decalage)
    print(f"Texte déchiffré : {dechiffre}")

def test_scytale():
    print("\n=== TEST DU CHIFFREMENT SCYTALE ===")
    texte_clair = "THISISASECRETMESSAGE"
    cle = 4  # Nombre de tours autour de la scytale
    print(f"Texte original : {texte_clair}")
    print(f"Clé (nombre de tours) : {cle}")
    
    chiffre = scytale.scytale_encrypt(texte_clair, cle)
    print(f"Texte chiffré : {chiffre}")
    
    dechiffre = scytale.scytale_decrypt(chiffre, cle)
    print(f"Texte déchiffré : {dechiffre}")

def test_polybius():
    print("\n=== TEST DU CARRÉ DE POLYBE ===")
    texte_clair = "HELLO"
    print(f"Texte original : {texte_clair}")
    
    chiffre = polybius.polybius_encrypt(texte_clair)
    print(f"Texte chiffré : {chiffre}")
    
    dechiffre = polybius.polybius_decrypt(chiffre)
    print(f"Texte déchiffré : {dechiffre}")

def test_affine():
    print("\n=== TEST DU CHIFFREMENT AFFINE ===")
    texte_clair = "HELLO"
    a, b = 5, 8  # Paramètres pour le chiffrement affine (a doit être premier avec 26)
    print(f"Texte original : {texte_clair}")
    print(f"Paramètres : a={a}, b={b}")
    
    chiffre = affine.affine_encrypt(texte_clair, a, b)
    print(f"Texte chiffré : {chiffre}")
    
    dechiffre = affine.affine_decrypt(chiffre, a, b)
    print(f"Texte déchiffré : {dechiffre}")

def test_vigenere():
    print("\n=== TEST DU CHIFFREMENT DE VIGENÈRE ===")
    texte_clair = "HELLOWORLD"
    cle = "KEY"
    print(f"Texte original : {texte_clair}")
    print(f"Clé : {cle}")
    
    chiffre = vigenere.vigenere_encrypt(texte_clair, cle)
    print(f"Texte chiffré : {chiffre}")
    
    dechiffre = vigenere.vigenere_decrypt(chiffre, cle)
    print(f"Texte déchiffré : {dechiffre}")

def main():
    while True:
        print("\n==== MENU PRINCIPAL - CHIFFREMENT CLASSIQUE ====")
        print("1. Chiffrement de César")
        print("2. Chiffrement Scytale")
        print("3. Carré de Polybe")
        print("4. Chiffrement Affine")
        print("5. Chiffrement de Vigenère")
        print("6. Exécuter tous les tests prédéfinis")
        print("0. Quitter")
        
        choix = input("\nEntrez votre choix (0-6): ")
        
        if choix == "0":
            print("Au revoir!")
            break
        
        elif choix == "1":
            print("\n--- CHIFFREMENT DE CÉSAR ---")
            action = input("Voulez-vous (c)hiffrer ou (d)échiffrer? ").lower()
            texte = input("Entrez votre texte: ").upper()
            decalage = int(input("Entrez le décalage (nombre entier): "))
            
            if action.startswith('c'):
                resultat = caesarscript.caesar_encrypt(texte, decalage)
                print(f"Texte chiffré: {resultat}")
            elif action.startswith('d'):
                resultat = caesarscript.caesar_decrypt(texte, decalage)
                print(f"Texte déchiffré: {resultat}")
            
        elif choix == "2":
            print("\n--- CHIFFREMENT SCYTALE ---")
            action = input("Voulez-vous (c)hiffrer ou (d)échiffrer? ").lower()
            texte = input("Entrez votre texte: ").upper()
            tours = int(input("Entrez le nombre de tours: "))
            
            if action.startswith('c'):
                resultat = scytale.scytale_encrypt(texte, tours)
                print(f"Texte chiffré: {resultat}")
            elif action.startswith('d'):
                resultat = scytale.scytale_decrypt(texte, tours)
                print(f"Texte déchiffré: {resultat}")
            
        elif choix == "3":
            print("\n--- CARRÉ DE POLYBE ---")
            action = input("Voulez-vous (c)hiffrer ou (d)échiffrer? ").lower()
            
            if action.startswith('c'):
                texte = input("Entrez votre texte: ").upper()
                resultat = polybius.polybius_encrypt(texte)
                print(f"Texte chiffré: {resultat}")
            elif action.startswith('d'):
                texte = input("Entrez les coordonnées (par ex. 1123453324): ")
                resultat = polybius.polybius_decrypt(texte)
                print(f"Texte déchiffré: {resultat}")
            
        elif choix == "4":
            print("\n--- CHIFFREMENT AFFINE ---")
            action = input("Voulez-vous (c)hiffrer ou (d)échiffrer? ").lower()
            texte = input("Entrez votre texte: ").upper()
            a = int(input("Entrez le paramètre a (doit être premier avec 26): "))
            b = int(input("Entrez le paramètre b: "))
            
            if action.startswith('c'):
                resultat = affine.affine_encrypt(texte, a, b)
                print(f"Texte chiffré: {resultat}")
            elif action.startswith('d'):
                resultat = affine.affine_decrypt(texte, a, b)
                print(f"Texte déchiffré: {resultat}")
            
        elif choix == "5":
            print("\n--- CHIFFREMENT DE VIGENÈRE ---")
            action = input("Voulez-vous (c)hiffrer ou (d)échiffrer? ").lower()
            texte = input("Entrez votre texte: ").upper()
            cle = input("Entrez la clé: ").upper()
            
            if action.startswith('c'):
                resultat = vigenere.vigenere_encrypt(texte, cle)
                print(f"Texte chiffré: {resultat}")
            elif action.startswith('d'):
                resultat = vigenere.vigenere_decrypt(texte, cle)
                print(f"Texte déchiffré: {resultat}")
                
        elif choix == "6":
            print("\nExécution de tous les tests prédéfinis...")
            test_caesar()
            test_scytale()
            test_polybius()
            test_affine()
            test_vigenere()
            
        else:
            print("Choix invalide. Veuillez réessayer.")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()