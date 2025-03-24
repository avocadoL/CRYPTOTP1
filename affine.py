def mod_inverse(a, m):
    """
    Calcule l'inverse modulaire de a modulo m.
    
    Args:
        a (int): Le nombre dont on cherche l'inverse
        m (int): Le modulo
    
    Returns:
        int: L'inverse modulaire de a modulo m, ou None si l'inverse n'existe pas
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    """
    Chiffre un texte en utilisant le chiffrement affine: C = (a*P + b) mod 26.
    
    Args:
        plaintext (str): Le texte clair à chiffrer
        a (int): Premier paramètre de la fonction affine (doit être premier avec 26)
        b (int): Second paramètre de la fonction affine
    
    Returns:
        str: Le texte chiffré
    """
    # Vérification que a est premier avec 26
    if mod_inverse(a, 26) is None:
        raise ValueError("La valeur de 'a' doit être première avec 26")
    
    plaintext = plaintext.upper()
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            # Conversion lettre -> nombre (A=0, B=1, ...)
            p_value = ord(char) - ord('A')
            # Application de la formule affine
            c_value = (a * p_value + b) % 26
            # Conversion nombre -> lettre
            ciphertext += chr(c_value + ord('A'))
        else:
            ciphertext += char
    
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Déchiffre un texte chiffré avec le chiffrement affine.
    
    Args:
        ciphertext (str): Le texte chiffré à déchiffrer
        a (int): Premier paramètre de la fonction affine
        b (int): Second paramètre de la fonction affine
    
    Returns:
        str: Le texte clair
    """
    # Calcul de l'inverse modulaire de a
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("La valeur de 'a' doit être première avec 26")
    
    ciphertext = ciphertext.upper()
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            # Conversion lettre -> nombre
            c_value = ord(char) - ord('A')
            # Application de la formule inverse: P = a^(-1) * (C - b) mod 26
            p_value = (a_inv * (c_value - b)) % 26
            # Conversion nombre -> lettre
            plaintext += chr(p_value + ord('A'))
        else:
            plaintext += char
    
    return plaintext 