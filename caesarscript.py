def caesar_encrypt(plaintext, shift):
    
    ciphertext = ""
    for char in plaintext:   
        ascii_offset = 65 if char.isupper() else 97
        shifted = (ord(char) - ascii_offset + shift) % 26
        ciphertext += chr(shifted + ascii_offset)    
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


if __name__ == "__main__":
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    
    encrypted = caesar_encrypt(text, shift)
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")

