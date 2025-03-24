def vigenere_encrypt(plaintext, key):
    """
    Chiffre un texte en utilisant le chiffrement de Vigenère.
    
    Args:
        plaintext (str): Le texte clair à chiffrer
        key (str): La clé de chiffrement
    
    Returns:
        str: Le texte chiffré
    """
    # Normalisation du texte et de la clé (conversion en majuscules)
    plaintext = plaintext.upper()
    key = key.upper()
    
    # Élimination des caractères non-alphabétiques
    plaintext_clean = ''.join(c for c in plaintext if c.isalpha())
    
    # Préparation de la clé répétée
    key_repeated = (key * (len(plaintext_clean) // len(key) + 1))[:len(plaintext_clean)]
    
    ciphertext = ""
    for i in range(len(plaintext_clean)):
        # Formule du chiffrement de Vigenère: (Pi + Ki) mod 26
        p_value = ord(plaintext_clean[i]) - ord('A')
        k_value = ord(key_repeated[i]) - ord('A')
        c_value = (p_value + k_value) % 26
        ciphertext += chr(c_value + ord('A'))
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """
    Déchiffre un texte chiffré avec le chiffrement de Vigenère.
    
    Args:
        ciphertext (str): Le texte chiffré à déchiffrer
        key (str): La clé de chiffrement
    
    Returns:
        str: Le texte clair
    """
    # Normalisation du texte et de la clé (conversion en majuscules)
    ciphertext = ciphertext.upper()
    key = key.upper()
    
    # Préparation de la clé répétée
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    
    plaintext = ""
    for i in range(len(ciphertext)):
        # Formule du déchiffrement de Vigenère: (Ci - Ki) mod 26
        c_value = ord(ciphertext[i]) - ord('A')
        k_value = ord(key_repeated[i]) - ord('A')
        p_value = (c_value - k_value) % 26
        plaintext += chr(p_value + ord('A'))
    
    return plaintext 