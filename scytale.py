def scytale_encrypt(plaintext, key):

    plaintext = ''.join(plaintext.upper().split())
    
    # Calcul du nombre de colonnes nécessaires
    # Le nombre de colonnes est égal à la longueur du texte divisée par la clé (arrondi au supérieur)
    columns = (len(plaintext) + key - 1) // key
    
    # Remplissage avec des X si nécessaire
    plaintext += 'X' * (columns * key - len(plaintext))
    
    # Construction de la matrice
    matrix = []
    for i in range(0, len(plaintext), columns):
        matrix.append(plaintext[i:i+columns])
    
    # Lecture par colonnes pour obtenir le texte chiffré
    ciphertext = ""
    for j in range(columns):
        for i in range(key):
            ciphertext += matrix[i][j]
    
    return ciphertext

def scytale_decrypt(ciphertext, key):
   
    columns = len(ciphertext) // key
    
    
    matrix = [[''] * columns for _ in range(key)]

    index = 0
    for j in range(columns):
        for i in range(key):
            matrix[i][j] = ciphertext[index]
            index += 1
    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)
    
    return plaintext
