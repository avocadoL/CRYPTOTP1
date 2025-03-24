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

    dechiffre = vigenere