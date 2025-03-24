def polybius_encrypt(plaintext):
    """
    Chiffre un texte en utilisant le carré de Polybe.
    
    Args:
        plaintext (str): Le texte clair à chiffrer
    
    Returns:
        str: Le texte chiffré sous forme de paires de chiffres
    """
    # Création du carré de Polybe 5x5 (I et J sont combinés)
    grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I/J', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    
    # Dictionnaire pour recherche rapide de coordonnées
    position = {}
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 'I/J':
                position['I'] = f"{i+1}{j+1}"
                position['J'] = f"{i+1}{j+1}"
            else:
                position[grid[i][j]] = f"{i+1}{j+1}"
    
    plaintext = plaintext.upper()
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char in position:
                ciphertext += position[char]
        else:
            # On peut choisir de garder ou ignorer les caractères non-alphabétiques
            pass
    
    return ciphertext

def polybius_decrypt(ciphertext):
    """
    Déchiffre un texte chiffré avec le carré de Polybe.
    
    Args:
        ciphertext (str): Le texte chiffré sous forme de paires de chiffres
    
    Returns:
        str: Le texte clair
    """
    # Création du carré de Polybe inversé (pour le déchiffrement)
    grid = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I/J', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    
    plaintext = ""
    
    # Vérification que la longueur du texte chiffré est paire
    if len(ciphertext) % 2 != 0:
        raise ValueError("Le texte chiffré doit contenir un nombre pair de chiffres")
    
    for i in range(0, len(ciphertext), 2):
        if ciphertext[i].isdigit() and ciphertext[i+1].isdigit():
            row = int(ciphertext[i]) - 1
            col = int(ciphertext[i+1]) - 1
            
            if 0 <= row < 5 and 0 <= col < 5:
                char = grid[row][col]
                if char == 'I/J':
                    plaintext += 'I'  # Convention: I est utilisé par défaut
                else:
                    plaintext += char
    
    return plaintext 