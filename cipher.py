def encrypt(plaintext, key_sequence):
    """
    Encrypts the plaintext using a sequence of numeric shifts (e.g. [6, 20, 11]).
    Only alphabetic characters are shifted; spaces and punctuation remain as is.
    Converts and processes everything in uppercase.
    """
    plaintext = plaintext.upper()
    ciphertext = []
    
    key_len = len(key_sequence)
    key_idx = 0
    
    for char in plaintext:
        if char.isalpha():
            # Convert letter to 0-25 scale
            p = ord(char) - ord('A')
            k_shift = key_sequence[key_idx % key_len]
            
            # Forward shift and modulo 26
            c = (p + k_shift) % 26
            
            # Convert back to character
            ciphertext.append(chr(c + ord('A')))
            
            # Increment shift sequence index
            key_idx += 1
        else:
            # Add spaces and punctuation directly
            ciphertext.append(char)
            
    return "".join(ciphertext)

def decrypt(ciphertext, key_sequence):
    """
    Decrypts the ciphertext using a sequence of numeric shifts (e.g. [6, 20, 11]).
    Only alphabetic characters are shifted; spaces and punctuation remain as is.
    Converts and processes everything in uppercase.
    """
    ciphertext = ciphertext.upper()
    plaintext = []
    key_len = len(key_sequence)
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            # Convert letter to 0-25 scale
            c = ord(char) - ord('A')
            k_shift = key_sequence[key_idx % key_len]
            # Reverse shift and modulo 26
            p = (c - k_shift) % 26
            # Convert back to character
            plaintext.append(chr(p + ord('A')))
            # Increment shift sequence index
            key_idx += 1
        else:
            # Add spaces and punctuation directly
            plaintext.append(char)

    return "".join(plaintext)
